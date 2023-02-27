import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet as p


class MOTOR:
    def __init__(self, jointName, bodyID):
        self.jointName = jointName
        self.bodyID = bodyID

    def Set_Value(self, desiredAngle):
         pyrosim.Set_Motor_For_Joint(
            bodyIndex = self.bodyID,
            jointName = self.jointName, 
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = c.Max_Force) 

