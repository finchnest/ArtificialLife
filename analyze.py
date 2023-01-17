import numpy as np
import matplotlib.pyplot as p


backLegSensorValues = np.load('data/back_values.npy')
frontLegSensorValues = np.load('data/front_values.npy')

p.plot(backLegSensorValues,  label='back sensor values', linewidth=10)
p.plot(frontLegSensorValues,  label='front sensor values')
p.legend()

p.show()


# print(backLegSensorValues)
