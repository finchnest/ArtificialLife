import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time

import constants as c

class SOLUTION:
    def __init__(self, myID):
        self.myID = myID

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
        randomRow = random.randint(0,self.num_sensors - 1)
        randomCol = random.randint(0,self.num_joints  - 1)
        self.weight[randomRow,randomCol] = random.random() * 2 - 1
       


    def Create_Body(self):

        pyrosim.Start_URDF("body.urdf")

        self.first_cube_size = [random.random(), random.random(), random.random()]        
        self.first_cube_pos = [0, 0, self.first_cube_size[1]/2]

        self.num_links = random.randint(1, 7)
        self.num_joints = self.num_links - 1


        self.links_with_sensor = []

        for x in range(0, self.num_links):
            coin = random.randint(0, 1)
            if coin == 1:
                self.links_with_sensor.append(x)

        

        print("links with sensor ", self.links_with_sensor)


        pyrosim.Send_Cube(name="Link0", pos=self.first_cube_pos, size=self.first_cube_size, color= 0 in self.links_with_sensor)

        pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0, self.first_cube_size[1]/2, self.first_cube_size[2]], jointAxis="1 0 0")

        for x in range(1, self.num_links):
            self.cube_size = [random.random(), random.random(), random.random()]
        
            pyrosim.Send_Cube(name="Link{}".format(x), pos=[0, self.cube_size[1] / 2, self.cube_size[2] / 2], size=self.cube_size, color= x in self.links_with_sensor)


            if x == self.num_links - 1:
                break
            pyrosim.Send_Joint(name="Link{}_Link{}".format(x, x + 1), parent="Link{}".format(x), child="Link{}".format(x + 1), type="revolute", position=[0, self.cube_size[1], self.cube_size[2]], jointAxis="1 0 0")


     
        pyrosim.End()



    def Create_Brain(self):

        os.system("rm brain*.nndf")
        os.system("rm fitness*.nndf")
        

        pyrosim.Start_NeuralNetwork("brain"+str(self.myID) +".nndf")


        self.num_sensors = 0
        for i in self.links_with_sensor:
            pyrosim.Send_Sensor_Neuron(name=self.num_sensors, linkName='Link{}'.format(i))
            self.num_sensors += 1

        for j in range(self.num_joints):
            pyrosim.Send_Motor_Neuron(name= j + self.num_sensors, jointName='Link{}_Link{}'.format(j, j + 1))

        self.weights = np.random.rand(self.num_sensors, self.num_joints)

        for i in range(self.num_sensors):
            for j in range(self.num_joints):
                pyrosim.Send_Synapse(sourceNeuronName= i, targetNeuronName= j + self.num_sensors, weight=self.weights[i, j])

        pyrosim.End()