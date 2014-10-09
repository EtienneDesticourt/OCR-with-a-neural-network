'''
Created on 9 Oct 2014
@author: Etienne
'''

from Network import *

###############################
#######UPDATE TEST#############
###############################

def testUpdate():
    
    input = [0.35,0.9] 
    MyNetwork = Network( (2,2,1) )
    
    MyNetwork.layers[0].nodes = np.array(input)
    MyNetwork.layers[1].weights = np.array([ [0.1,0.8],[0.4,0.6] ])
    MyNetwork.layers[2].weights = np.array([ [0.3,0.9] ])
       
    MyNetwork.update()      
#############END###############

###############################
######BACKPROP TEST############
###############################

def testBackprop():
    
    input = [0.35,0.9] 
    MyNetwork = Network( (2,2,1) )
    
    MyNetwork.layers[0].nodes = np.array(input)
    MyNetwork.layers[1].weights = np.array([ [0.1,0.8],[0.4,0.6] ])
    MyNetwork.layers[2].weights = np.array([ [0.3,0.9] ])
       
    print MyNetwork.update()
    for i in xrange(500):
        MyNetwork.backprop([0.5])
        MyNetwork.update() 
    print MyNetwork.update()      
#############END###############

###############################
######BACKPROP TEST############
###############################

def testBackprop2():
    
    input = [1,0,1,0] 
    MyNetwork = Network( (4,3,2) )
    
    MyNetwork.layers[0].nodes = np.array(input)
    MyNetwork.layers[1].weights = np.array([ [0.1,0.8],[0.4,0.6] ])
    MyNetwork.layers[2].weights = np.array([ [0.3,0.9] ])
       
    print MyNetwork.update()
    for i in xrange(500):
        MyNetwork.backprop([0.5])
        MyNetwork.update() 
    print MyNetwork.update()      
#############END###############






###########RUN TEST############

#testUpdate()
# testBackprop()

###############################




