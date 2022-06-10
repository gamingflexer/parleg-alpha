import os
import sys

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


os.environ['PYTHONPATH'] += "/Users/cosmos/Desktop/parleg-alpha/RealTimeObjectDetection/Tensorflow/models"


sys.path.append( "/Users/cosmos/Desktop/parleg-alpha/RealTimeObjectDetection/Tensorflow/models")

SAVING_FRAMES_PER_SECOND = 0.5