from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c


class SIMULATION:

    def __init__(self):

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):

        for x in range(c.ITERATION):
            p.stepSimulation()
            time.sleep( 1/60 )

            self.robot.Sense(x)

            self.robot.Think()

            self.robot.Act(x)

           

    def __del__(self):
        p.disconnect()
    