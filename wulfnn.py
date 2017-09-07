# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 08:14:50 2017

@author: Nicholas
"""
from numpy import array, exp
from random import random

def Sigmoid(activation, response=1):
    return 1/(1 + exp(-activation/response))

class wulfNeuralNet:
    def __init__(self, NumInputs, NumOutputs, NumHiddenLayers, NeuronPerHiddenLyr):
        self.Layers = array([[[random()]*(NumInputs+1)]*NeuronPerHiddenLyr]*NumHiddenLayers)
    def Update(self, inputs):
        outputs = []
        if len(inputs) != len(self.Layers[0]):
            return outputs
        for i in range(len(self.Layers)):
            if i > 0:
                for j in range(len(outputs)):
                    inputs[j] = outputs[j]
            del outputs[:]
            print(inputs)
            Layer = self.Layers[i]
            NumNeurons = len(Layer)
            for j in range(NumNeurons):
                netinput = 0.0
                Neuron = Layer[j]
                NumInputs = len(Neuron)
                for k in range(NumInputs-1):
                    netinput += Neuron[k] * inputs[k]
                netinput += Neuron[-1] * (-1.0)
                outputs.append(Sigmoid(netinput))
        self.Outputs = outputs
        return array(outputs)

if __name__ == "__main__":
    nn = wulfNeuralNet(3,3,9,3)
    print(nn.Update(array([0.5,0.8,0.5])))
