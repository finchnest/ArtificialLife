import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import time
import math
import random


front_amplitude = np.pi/4
front_frequency = 10
front_phaseOffset = 0

back_amplitude = np.pi/4
back_frequency = 10
back_phaseOffset = np.pi/4

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)



planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)


backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

np.save('data/back_values.npy', backLegSensorValues)
np.save('data/front_values.npy', frontLegSensorValues)

front_targetAngles = front_amplitude * np.sin(front_frequency * np.linspace(0, 2*np.pi, 1000 ) + front_phaseOffset)

back_targetAngles = back_amplitude * np.sin(back_frequency * np.linspace(0, 2*np.pi, 1000 ) + back_phaseOffset)

# np.save('data/front_targetAngles.npy', front_targetAngles)
# np.save('data/back_targetAngles.npy', back_targetAngles)
# exit ()

for x in range(1000):
    p.stepSimulation()
    time.sleep( 1/60 )


    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("Link2")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("Link1")

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = "Link0_Link2", 
    controlMode = p.POSITION_CONTROL,
    targetPosition = back_targetAngles[x],
    maxForce = 500)

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = "Link0_Link1", 
    controlMode = p.POSITION_CONTROL,
    targetPosition = front_targetAngles[x],
    maxForce = 500)


p.disconnect()