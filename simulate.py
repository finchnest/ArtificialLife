import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import time


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)


backLegSensorValues = np.zeros(100)
frontLegSensorValues = np.zeros(100)

# print(backLegSensorValues)
# exit()

for x in range(100):
    p.stepSimulation()
    time.sleep( 1/60 )

    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("Link2")
    frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("Link1")

    backLegSensorValues[x] = backLegTouch
    frontLegSensorValues[x] = frontLegTouch

    # print(backLegTouch)
    # print(x)
    # print(backLegSensorValues)

np.save('data/back_values.npy', backLegSensorValues)
np.save('data/front_values.npy', frontLegSensorValues)


p.disconnect()