from darkflow.darkflow.defaults import argHandler #Import the default arguments
import os
from darkflow.darkflow.net.build import TFNet


FLAGS = argHandler()
FLAGS.setDefaults()

FLAGS.demo = "test_2.avi" # video file to use, or if camera just put "camera"
FLAGS.model = "darkflow/cfg/yolo.cfg" # tensorflow model
FLAGS.load = "darkflow/bin/yolo.weights" # tensorflow weights
FLAGS.threshold = 0.25 # threshold of decetion confidance (detection if confidance > threshold )
FLAGS.gpu = 0.75 #how much of the GPU to use (between 0 and 1) 0 means use cpu , FPS on CPU (i5) : 0.5 /  FPS on GPU (8Go) : 15 (leave .3 for the tracker)
FLAGS.track = False # wheither to activate tracking or not
FLAGS.trackObj = "person" # the object to be tracked
FLAGS.saveVideo = False  #whether to save the video or not
FLAGS.BK_MOG = False # activate background substraction using MOG substraction, if False we will be using YOLO , if TRue we will use BG
FLAGS.skip = 1 # how many frames to skipp between each detection to speed up the network
FLAGS.csv = False #whether to write csv file or not(only when tracking is set to True)

tfnet = TFNet(FLAGS)

tfnet.camera()
exit('Demo stopped, exit.')
