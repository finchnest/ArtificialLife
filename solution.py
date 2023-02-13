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
        pyrosim.Send_Cube(name="Box", pos=[-4,0,0.5] , size=[1, 1, 1])
        pyrosim.End()


    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons - 1)
        randomCol = random.randint(0,c.numMotorNeurons  - 1)
        self.weight[randomRow,randomCol] = random.random() * 2 - 1
       


    def Create_Body(self):

        pyrosim.Start_URDF("body.urdf")

        first_cube_size = [random.random(), random.random(), random.random()]        
        first_cube_pos = [0, first_cube_size[1]/2, 0]

        self.num_links = 10 #random.randint(1, 10)
        self.num_joints = self.num_links - 1

        #randomly assign sensors to links

        self.links_with_sensor = []

        for j in range(self.num_links):
            self.links_with_sensor.append(random.randint(0, 1))
        print("links with sensor ", self.links_with_sensor)


        pyrosim.Send_Cube(name="Link0", pos=first_cube_pos, size=first_cube_size, color= (True if self.links_with_sensor[0] == 1 else False))
        pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0, first_cube_size[1]/2, first_cube_size[2]], jointAxis="1 0 0")

        for x in range(1, self.num_links):
            cube_size = [random.random(), random.random(), random.random()]
        
            pyrosim.Send_Cube(name="Link{}".format(x), pos=[0, cube_size[1] / 2, cube_size[2] / 2], size=cube_size, color=(True if self.links_with_sensor[x] == 1 else False))

            #additional will be created in the last iteration.
            pyrosim.Send_Joint(name="Link{}_Link{}".format(x, x + 1), parent="Link{}".format(x), child="Link{}".format(x + 1), type="revolute", position=[0, cube_size[0], cube_size[2]], jointAxis="1 0 0")


     
        pyrosim.End()



    def Create_Brain(self):


        pyrosim.Start_NeuralNetwork("brain"+str(self.myID) +".nndf")

        self.name = 0

        for y in range(len(self.links_with_sensor)):
            if(self.links_with_sensor[y] == 1):
                pyrosim.Send_Sensor_Neuron(name = self.name , linkName='Link{}'.format(y))
            self.name +=1
        
        for i in range(self.num_joints):
            pyrosim.Send_Motor_Neuron(name=i + self.name, jointName='Link{}_Link{}'.format(i, i+1))
            self.name +=1


        self.sensors_count = np.count_nonzero(np.array(self.links_with_sensor))
    
    
        self.weights = np.random.rand(self.sensors_count, self.num_joints)




        for sensor in range(self.sensors_count):
            for motor in range(self.num_joints):
                pyrosim.Send_Synapse(sourceNeuronName = sensor, targetNeuronName = motor + self.sensors_count, weight = self.weight[sensor,motor] )

        pyrosim.End()