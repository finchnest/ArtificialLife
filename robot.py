import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import constants as c

from pyrosim.neuralNetwork import NEURAL_NETWORK

import os

class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID

        brain = "brain" + str(self.solutionID) + ".nndf"
        self.fitness = "fitness" + str(self.solutionID) + ".txt"
        self.tmp = "tmp" + str(self.solutionID) + ".txt"
        body = "body" + str(self.solutionID) + ".urdf"

        self.robotID = p.loadURDF(body)
        self.nn = NEURAL_NETWORK(brain)


        pyrosim.Prepare_To_Simulate(self.robotID)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        os.system("rm "+ brain)      
        os.system("rm "+ body)


    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self, x):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(x) 

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotID, 0)
        position0fLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = position0fLinkZero[0]

        f = open(self.tmp,'w')
        f.write(str(xCoordinateOfLinkZero))

        f.close()

        os.system("mv "+ self.tmp +" "+ self.fitness)
        
    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName, self.robotID)
    
    def Act(self, x):

        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle)

    def Think(self):
        
        self.nn.Update()
        # self.nn.Print()
        




        