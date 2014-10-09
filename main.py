from Network import *
from PIL import Image
from math import ceil
import os
  
PATH = "Drawing\\Dataset"
NUMBEXAMPLES = 38



#LOAD DATASET
A,B = [],[]

for i in os.listdir(PATH):    
    img = Image.open(PATH+"\\"+i)
    
    #Transforms image into binary array
    pixdata = img.getdata()        
    data = []    
    for j in pixdata: 
        if j == (0,0,0): data.append(1.0) #The characters are written in black on a white background
        else:            data.append(0.0)
    
    if "A" in i:         A.append(np.array(data))
    else:                B.append(np.array(data))
  

dataset = [A,B]
  
#CREATE NETWORK
MyNetwork = Network( size=(81,50,1) ) # 9x9 images so 81 input, hidden network length was found by trial and error. 

#TRAIN NETWORK
def train(numbExamples):
    print MyNetwork.update()
       
    print "New example:", os.listdir(PATH)[numbExamples-1]
    for i in xrange(100):
        for example in xrange(numbExamples):
            for target in xrange(2):
                MyNetwork.layers[0].nodes = dataset[target][example]
                MyNetwork.update(),target
                MyNetwork.backprop([target], 1)
           
def calcAccuracy(testRange):
    total = len(testRange)*2
    correct = 0.0
    for example in testRange:
        for target in xrange(2):
            MyNetwork.layers[0].nodes = dataset[target][example]
            result = MyNetwork.update() > 0.5
            if result == target:
                correct += 1            
    print correct/total*100
    
mustLoad = raw_input("Load (y/n)? Otherwise the network will be trained. \n")
if mustLoad == "y":
    MyNetwork.load()
else:
    MyNetwork.train(NUMBEXAMPLES)


calcAccuracy(range(39,48))

