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

        self.brain = "brain"+str(self.solutionID)+".nndf"
        self.fitness = "fitness"+str(self.solutionID)+".txt"
        self.tmp = "tmp"+str(self.solutionID)+".txt"

        self.robot = p.loadURDF("body.urdf")

        self.nn = NEURAL_NETWORK(self.brain)


        pyrosim.Prepare_To_Simulate(self.robot)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        os.system("rm "+ self.brain)



    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self, x):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(x) 

    def Get_Fitness(self):
        self.stateOfLinkZero = p.getLinkState(self.robot, 0)
        self.position0fLinkZero = self.stateOfLinkZero[0]
        self.xCoordinateOfLinkZero = self.position0fLinkZero[0]

        f = open('fitness'+str(self.solutionID)+'.txt','w')
        f.write(str(self.xCoordinateOfLinkZero))
        f.close()

        os.system("mv "+ self.tmp +" "+ self.fitness)
        
    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            if jointName == 'Link0_Link1':
                self.motors[jointName] = MOTOR(jointName,frequency= c.back_frequency/2)
            else:
                self.motors[jointName] = MOTOR(jointName)
    
    def Act(self, x):

        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)

                self.motors[jointName].Set_Value(self.robot, desiredAngle)

    def Think(self):
        
        self.nn.Update()
        # self.nn.Print()
        




        