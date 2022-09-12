from config import * 
import imutils
import os
import sys
import cv2 
import numpy as np
from PIL import Image
from matplotlib.image import imread
import tensorflow as tf
from matplotlib import pyplot as plt
from object_detection.utils import config_util
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder


# Load pipeline config and build a detection model
configs = config_util.get_configs_from_pipeline_file(CONFIG_PATH)
detection_model = model_builder.build(model_config=configs['model'], is_training=False)

# Restore checkpoint
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(os.path.join(CHECKPOINT_PATH, 'ckpt-50')).expect_partial()

@tf.function
def detect_fn(image):
    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)
    return detections

category_index = label_map_util.create_category_index_from_labelmap(ANNOTATION_PATH+'/label_map.pbtxt')

dataset = 'Valour3'
frameNo = '62'


def detect_part(image_np):
    
    #crop
    
    coordinates = []
    max_boxes_to_draw = 5
    min_score_thresh=.3

    input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
    #print(input_tensor.shape)
    detections = detect_fn(input_tensor)

    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy()
                for key, value in detections.items()}
    detections['num_detections'] = num_detections

    # print(detections['detection_classes'])
    # print(type(detections['detection_classes']))
    # detection_classes should be ints.
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

    imgout = Image.fromarray(image_np, 'RGB')
    
    #cropping
    
    boxes = detections['detection_boxes']
    # max_boxes_to_draw = boxes.shape[0]
    scores = detections['detection_scores']


    for i in range(min(max_boxes_to_draw, boxes.shape[0])):
        if scores[i] > min_score_thresh:
            class_id = int(detections['detection_classes'][i] + 1)
            box = boxes[i]
            im_height = imgout.height
            im_width = imgout.width
            (ymin, xmin, ymax, xmax) = (box[0] * im_height, box[1] * im_width,
                            box[2] * im_height, box[3] * im_width)
            coordinates.append({
                "box": [int(xmin) , int(ymin) , int(xmax) ,int(ymax)],
                "class_name": category_index[class_id]["name"],
                "score": scores[i]
            })
    return imgout,coordinates


def translate_box(coordinates):
    try:
        left,upper,right,lower = coordinates[0]['box']
        for coordinate in coordinates:
            if coordinate['class_name']=="arrow":
                left,upper,right,lower = coordinate['box']
                new_upper = upper - (lower-upper)
                right = right + (right-left)*0.2
                lower = lower - (lower-upper)
                return (left,new_upper,right,lower)
    except:
        pass 
        
        
