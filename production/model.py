CURRENT_WORKSPACE_NAME = '/workspace'
ROOT_PATH = '/Users/cosmos/Desktop/parleg-alpha/RealTimeObjectDetection'
WORKSPACE_PATH = ROOT_PATH+'/Tensorflow/'+CURRENT_WORKSPACE_NAME
SCRIPTS_PATH = ROOT_PATH+'/Tensorflow/scripts'
APIMODEL_PATH = ROOT_PATH+'/Tensorflow/models'
ANNOTATION_PATH = WORKSPACE_PATH+'/annotations'
IMAGE_PATH = WORKSPACE_PATH+'/images'
MODEL_PATH = WORKSPACE_PATH+'/models'
PRETRAINED_MODEL_PATH = WORKSPACE_PATH+'/pre-trained-models'
CONFIG_PATH = MODEL_PATH+'/my_ssd_mobnet/pipeline.config'
CHECKPOINT_PATH = MODEL_PATH+'/my_ssd_mobnet/'

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


os.environ['PYTHONPATH'] += "/Users/cosmos/Desktop/parleg-alpha/RealTimeObjectDetection/Tensorflow/models"


sys.path.append( "/Users/cosmos/Desktop/parleg-alpha/RealTimeObjectDetection/Tensorflow/models")

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


def detect(frame):
    img = imread(frame)
    # print(type(img))

    image_np = np.array(img)
    # print(type(image_np))

    input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
    detections = detect_fn(input_tensor)

    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy()
                for key, value in detections.items()}
    detections['num_detections'] = num_detections

    # print(detections['detection_classes'])
    # print(type(detections['detection_classes']))

    # detection_classes should be ints.
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

    label_id_offset = 1
    image_np_with_detections = image_np.copy()

    viz_utils.visualize_boxes_and_labels_on_image_array(
                image_np_with_detections,
                detections['detection_boxes'],
                detections['detection_classes']+label_id_offset,
                detections['detection_scores'],
                category_index,
                use_normalized_coordinates=True,
                max_boxes_to_draw=5,
                min_score_thresh=.3,
                agnostic_mode=False)

    imgout = Image.fromarray(image_np_with_detections, 'RGB')
    imgout.save('output.png')
    
    
    #Cordinates
    coordinates = []
    max_boxes_to_draw = 5
    min_score_thresh=.3
    boxes = detections['detection_boxes']
    # max_boxes_to_draw = boxes.shape[0]

    scores = detections['detection_scores']


    for i in range(min(max_boxes_to_draw, boxes.shape[0])):
        if scores[i] > min_score_thresh:
            class_id = int(detections['detection_classes'][i] + 1)
            coordinates.append({
                "box": boxes[i],
                "class_name": category_index[class_id]["name"],
                "score": scores[i]
            })

    print("Detection done")
    return coordinates


