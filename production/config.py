import os
import sys


basepath = os.path.dirname(os.path.realpath(__file__))

CURRENT_WORKSPACE_NAME = '/workspace'
ROOT_PATH = '/Users/cosmos/Desktop/Projects/parleg-alpha/RealTimeObjectDetection'
WORKSPACE_PATH = ROOT_PATH+'/Tensorflow/'+CURRENT_WORKSPACE_NAME
SCRIPTS_PATH = ROOT_PATH+'/Tensorflow/scripts'
APIMODEL_PATH = ROOT_PATH+'/Tensorflow/models'
ANNOTATION_PATH = WORKSPACE_PATH+'/annotations'
IMAGE_PATH = WORKSPACE_PATH+'/images'
MODEL_PATH = WORKSPACE_PATH+'/models'
PRETRAINED_MODEL_PATH = WORKSPACE_PATH+'/pre-trained-models'
CONFIG_PATH = MODEL_PATH+'/my_ssd_mobnet/pipeline.config'
CHECKPOINT_PATH = MODEL_PATH+'/my_ssd_mobnet/'


# os.environ['PYTHONPATH'] += "/Users/cosmos/Desktop/parleg-alpha/RealTimeObjectDetection/Tensorflow/models"


sys.path.append( "/Users/cosmos/Desktop/Projects/parleg-alpha/RealTimeObjectDetection/Tensorflow/models")

SAVING_FRAMES_PER_SECOND = 1

Video_path = os.path.join(basepath,"data","test_video.mp4")

CSV_PATH = os.path.join(basepath,"data","output.csv")