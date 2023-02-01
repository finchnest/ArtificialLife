import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5



class SOLUTION:
    def __init__(self, myID):
        self.myID = myID
        self.weight = 2 * (np.random.rand(3, 2) - 1)
    def Set_ID(self,ID):
        self.myID = ID
    def Evaluate(self, GUI):

        
        self.Start_Simulation(GUI)
        self.Wait_For_Simulation_To_End()

        

    def Start_Simulation(self, GUI):
        self.directOrGUI = "GUI " if GUI else "DIRECT "
        # print("--- command about to run ----", self.ctr)

       
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system("python3 simulate.py "+ self.directOrGUI +str(self.myID)+ " &")



    def Wait_For_Simulation_To_End(self):
        self.fitnessFileName = "fitness"+str(self.myID)+".txt"
        while not os.path.exists(self.fitnessFileName):

            time.sleep(0.01)
        
        with open(self.fitnessFileName,"r") as fitness_info :
            self.fitness = float(fitness_info.read())

            print("fitness value is ==> ", self.fitness)
        os.system("rm "+ self.fitnessFileName)


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-4,y,z] , size=[length, width, height])
        pyrosim.End()


    def Mutate(self):
        randomRow = random.randint(0,2)
        randomCol = random.randint(0,1)
        self.weight[randomRow,randomCol] = random.random() * 2 - 1


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")



        pyrosim.Send_Cube(name="Link0", pos=[0, 0, 1.5], size=[length, width, height])
        
        pyrosim.Send_Joint(name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position =  [0.5,0,1])

        pyrosim.Send_Cube(name="Link1", pos= [0.5, 0, -0.5] , size=[length, width, height])
        

        pyrosim.Send_Joint(name = "Link0_Link2" , parent= "Link0" , child = "Link2" , type = "revolute", position = [-0.5, 0, 1])
        
        pyrosim.Send_Cube(name="Link2", pos=[-0.5, 0, -0.5] , size=[length, width, height])

        pyrosim.End()



    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID) +".nndf")
        
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Link0")

        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "Link1")

        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "Link2")

        pyrosim.Send_Motor_Neuron( name = 3, jointName = "Link0_Link1")
        
        pyrosim.Send_Motor_Neuron( name = 4, jointName = "Link0_Link2")


        for sensor in range(3):
            for motor in range(2):
                pyrosim.Send_Synapse( sourceNeuronName = sensor , targetNeuronName = motor+3 , weight = self.weight[sensor,motor] )

        pyrosim.End()