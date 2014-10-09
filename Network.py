



from Layer import Layer
import numpy as np

class Network:
    def __init__(self,size):
        self.layers = []        
        self.layers.append( Layer(size[0],1) )
        for i in xrange(len(size)-1):
            self.layers.append( Layer(size[i+1],size[i]) )
        self.layerNumber = len(self.layers)
    def save(self):        
        np.save("hidden.npy",self.layers[1].weights)
        np.save("output.npy",self.layers[2].weights)
    def load(self):
        self.layers[1].weights = np.load("hidden.npy")
        self.layers[2].weights = np.load("output.npy")
    def activation(self,array):
        return 1.0/ (np.exp( -array ) + 1)
    def setInput(self,input):
        self.layers[0].nodes = input
    def update(self):
        for i in xrange(self.layerNumber-1):
            layer = self.layers[i+1]
            lastLayer = self.layers[i]            
            weighted = lastLayer.nodes * layer.weights 
            layer.nodes = self.activation( weighted.sum(axis=1) )
        return layer.nodes       
    def backprop(self,targets,learningRate=1):
        outputLayer = self.layers[-1]
        hiddenLayer = self.layers[1]
        inputLayer = self.layers[0]
        
        ###########DELTAS###############
        
        oDeltas = (targets-outputLayer.nodes)*(1-outputLayer.nodes)*outputLayer.nodes
        hDeltas = (oDeltas*outputLayer.weights).sum() * (1-hiddenLayer.nodes)*hiddenLayer.nodes
        
        ###########WEIGHTS#############
        
        
        outputLayer.weights += learningRate * np.outer(oDeltas,hiddenLayer.nodes)
        hiddenLayer.weights += learningRate * np.outer(hDeltas,inputLayer.nodes)
        
        
