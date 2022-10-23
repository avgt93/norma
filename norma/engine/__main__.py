import sys

from .model import Model
from .connector import launch_executor
from .gamesimulation import Simulator
import os
from .constants import GOATMODELPATH, TARGETMODELPATH, TIGERMODELPATH 
from bagchal import Bagchal
import tensorflow

if len(sys.argv) == 1:
    print("Missing arguments!")
    print("Please use `train` or `serve` !")
    exit(0)

if sys.argv[1] == "train":
    if len(sys.argv) == 3:
        if (sys.argv[2] == "clean"):
            simulator = Simulator()
            simulator.simulate()

        elif (sys.argv[2] == "goat"):
            tigerModel = Model()
            tigerModel.model.set_weights(tensorflow.keras.models.load_model(TARGETMODELPATH).get_weights())
            simulator = Simulator(tigerModel=tigerModel)
            simulator.goatsimulate()
    else: 
        if not os.path.exists(TARGETMODELPATH):
            simulator = Simulator()
            simulator.simulate()
        else:
            loadModel = tensorflow.keras.models.load_model(TARGETMODELPATH)
            simulator = Simulator()
            simulator.simulate(targetModel= loadModel)
        

elif sys.argv[1] == "serve":
    launch_executor()
