import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import constants as c

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self, x):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(x) 

    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            if jointName == 'Link0_Link1':
                self.motors[jointName] = MOTOR(jointName,frequency= c.back_frequency/2)
            else:
                self.motors[jointName] = MOTOR(jointName)
    
    def Act(self, x):
        for jointName in self.motors:
            self.motors[jointName].Set_Value(self.robotId, x)


        