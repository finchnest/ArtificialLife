import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet as p


class MOTOR:
    def __init__(self, jointName, amplitude = c.amplitude, frequency = c.frequency,offset = c.phaseOffset):
        self.jointName = jointName

        self.amplitude = amplitude
        self.frequency = frequency
        self.offset = offset

        # self.Prepare_To_Act()

    # def Prepare_To_Act(self):
    #     self.motorValues = self.amplitude * np.sin(self.frequency * np.linspace(0, 2*np.pi, c.ITERATION ) + self.offset)

    def Set_Value(self, robotId, desiredAngle):
         pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName, 
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 500) 

    # def Save_Values(self):
    #     np.save('data/'+self.jointName +'_targetAngles.npy',self.motorValues)
 

