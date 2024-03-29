import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time

import constants as c

class SOLUTION:
    def __init__(self, myID):
        self.myID = myID
        self.weight = 5 * (np.random.rand(c.numSensorNeurons, c.numMotorNeurons) - 1)

        self.innerLegs = [0.2,0.2,1]
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

        os.system("python3 simulate.py "+ self.directOrGUI +str(self.myID)+ " 2&>log.log &")


    def Wait_For_Simulation_To_End(self):
        self.fitnessFileName = "fitness"+str(self.myID)+".txt"
        while not os.path.exists(self.fitnessFileName):

            time.sleep(0.01)
        
        with open(self.fitnessFileName,"r") as fitness_info :
            self.fitness = float(fitness_info.read())

        os.system("rm "+ self.fitnessFileName)


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-4,0,0.5] , size=[1, 1, 1])
        pyrosim.End()


    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons - 1)
        randomCol = random.randint(0,c.numMotorNeurons  - 1)
        self.weight[randomRow,randomCol] = random.random() * 2 - 1
        self.innerLegs = [
            np.random.uniform(low=0.2, high=0.6, size=1) * 2 - 1, 
            np.random.uniform(low=0.2, high=0.6, size=1) * 2 - 1,
            np.random.uniform(low=0.7, high=1.3, size=1) * 2 - 1

            ]


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0,0,1], size = [1,1,0.5])

        #Front_upper
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",child="FrontLeg", type="revolute",position=[0,0.5,1],jointAxis='1 0 0')
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0], size = [0.2,1,0.2])

        #Front_lower
        pyrosim.Send_Joint(name="FrontLeg_LowerFrontLeg", parent="FrontLeg",child="LowerFrontLeg", type="revolute",position=[0, 1, 0],jointAxis='0 1 0')
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0,0,-0.5], size = self.innerLegs)


        ###



        #FR
        pyrosim.Send_Joint(name="Torso_FRLowerLeg", parent="Torso",child="FRLowerLeg", type="revolute",position=[0.5,0.5,1],jointAxis='1 1 0')
        pyrosim.Send_Cube(name="FRLowerLeg", pos=[0,0,-0.5], size = self.innerLegs)
        #FL
        pyrosim.Send_Joint(name="Torso_FLLowerLeg", parent="Torso",child="FLLowerLeg", type="revolute",position=[-0.5,0.5,1],jointAxis='0 1 1')
        pyrosim.Send_Cube(name="FLLowerLeg", pos=[0,0,-0.5], size = self.innerLegs)
        #BR
        pyrosim.Send_Joint(name="Torso_BRLowerLeg", parent="Torso",child="BRLowerLeg", type="revolute",position=[0.5,-0.5,1],jointAxis='1 0 0')
        pyrosim.Send_Cube(name="BRLowerLeg", pos=[0,0,-0.5], size = self.innerLegs)
        #BL
        pyrosim.Send_Joint(name="Torso_BLLowerLeg", parent="Torso",child="BLLowerLeg", type="revolute",position=[-0.5,-0.5,1],jointAxis='0 0 1')
        pyrosim.Send_Cube(name="BLLowerLeg", pos=[0,0,-0.5], size = self.innerLegs)



        ### Many legs make light work ###


        #Back_upper
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso",child="BackLeg", type="revolute",position=[0, -0.5, 1],jointAxis='1 0 0')
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0], size = [0.2,1,0.2])

        #Back_lower
        pyrosim.Send_Joint(name="BackLeg_LowerBackLeg", parent="BackLeg",child="LowerBackLeg", type="revolute",position=[0, -1, 0],jointAxis='0 1 0')
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0,0,-0.5], size = self.innerLegs)


        #Right_upper
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso",child="RightLeg", type="revolute",position=[0.5, 0, 1],jointAxis='0 1 0')
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0], size = [1,0.2,0.2])

        #Right_lower
        pyrosim.Send_Joint(name="RightLeg_LowerRightLeg", parent="RightLeg",child="LowerRightLeg", type="revolute",position=[1, 0, 0],jointAxis='1 0 0')
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0,0,-0.5], size = self.innerLegs)

        #Left_upper
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso",child="LeftLeg", type="revolute",position=[-0.5, 0, 1],jointAxis='0 1 0')
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0], size = [1,0.2,0.2])

        #Left_lower
        pyrosim.Send_Joint(name="LeftLeg_LowerLeftLeg", parent="LeftLeg",child="LowerLeftLeg", type="revolute",position=[-1, 0, 0],jointAxis='1 0 0')
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0,0,-0.5], size = self.innerLegs)


        pyrosim.End()



    def Create_Brain(self):


        pyrosim.Start_NeuralNetwork("brain"+str(self.myID) +".nndf")
        
        # pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")

        # pyrosim.Send_Sensor_Neuron(name = 1, linkName = "FrontLeg")

        # pyrosim.Send_Sensor_Neuron(name = 2, linkName = "BackLeg")

        # pyrosim.Send_Motor_Neuron( name = 3, jointName = "Torso_FrontLeg")
        
        # pyrosim.Send_Motor_Neuron( name = 4, jointName = "Torso_BackLeg")

        self.sensors = ["LowerLeftLeg", "LowerRightLeg", "LowerFrontLeg", "LowerBackLeg", "FRLowerLeg", "FLLowerLeg", "BRLowerLeg", "BLLowerLeg"]
        self.joints = ["Torso_FrontLeg", "FrontLeg_LowerFrontLeg", "Torso_BackLeg", "BackLeg_LowerBackLeg", "Torso_RightLeg" , "RightLeg_LowerRightLeg", "Torso_LeftLeg","LeftLeg_LowerLeftLeg", 
        "Torso_FRLowerLeg", "Torso_FLLowerLeg", "Torso_BRLowerLeg", "Torso_BLLowerLeg"
        ]

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