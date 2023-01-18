import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values  = np.zeros(c.ITERATION)
    def Get_Value(self, x):
        self.values[x] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
    def Print_Sensor_Values(self):
        print(self.linkName, self.values)
    
    def save_values(self):
        np.save('data/'+self.linkName +'_sensorValues.npy',self.values)