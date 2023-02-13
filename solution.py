import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time

import constants as c

class SOLUTION:
    def __init__(self, myID):
        self.myID = myID
        self.weight = 1 * (np.random.rand(c.numSensorNeurons, c.numMotorNeurons) - 1)

    def Set_ID(self,ID):
        self.myID = ID
    def Evaluate(self, GUI):
        
        self.Start_Simulation(GUI)
        self.Wait_For_Simulation_To_End()


    def Start_Simulation(self, GUI):
        self.directOrGUI = "GUI " if GUI else "DIRECT "

        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system("python3 simulate.py " + self.directOrGUI + str(self.myID) + " 2&>log.log &")


    def Wait_For_Simulation_To_End(self):
        self.fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(self.fitnessFileName):
            time.sleep(0.01)
        with open(self.fitnessFileName,"r") as fitness_info :
            self.fitness = float(fitness_info.read())

        os.system("rm "+ self.fitnessFileName)


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        # pyrosim.Send_Cube(name="Box", pos=[-4,0,0.5] , size=[1, 1, 1])
        pyrosim.End()


    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons - 1)
        randomCol = random.randint(0,c.numMotorNeurons  - 1)
        self.weight[randomRow,randomCol] = random.random() * 2 - 1
       


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        box_size = [random.random(), random.random(), random.random()]



     
        pyrosim.End()



    def Create_Brain(self):


        pyrosim.Start_NeuralNetwork("brain"+str(self.myID) +".nndf")


        self.sensors = []
        self.joints = []

        self.name = 0
        for link in range(len(self.sensors)) :
            pyrosim.Send_Sensor_Neuron(name = self.name , linkName = self.sensors[link])
            self.name += 1
        for joint in range(len(self.joints)) :
            pyrosim.Send_Motor_Neuron(name =self.name , jointName = self.joints[joint])
            self.name += 1


        for sensor in range(len(self.sensors)):
            for motor in range(len(self.joints)):
                pyrosim.Send_Synapse(sourceNeuronName = sensor, targetNeuronName = motor + len(self.sensors), weight = self.weight[sensor,motor] )

        pyrosim.End()