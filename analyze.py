import numpy as np
import matplotlib.pyplot as p


backLegSensorValues = np.load('data/back_values.npy')
frontLegSensorValues = np.load('data/front_values.npy')

front_targetAngles = np.load('data/front_targetAngles.npy')
back_targetAngles = np.load('data/back_targetAngles.npy')


# p.plot(backLegSensorValues,  label='back sensor values', linewidth=10)
# p.plot(frontLegSensorValues,  label='front sensor values')
# p.legend()
# p.show()



p.plot(front_targetAngles,  label='front target Angles')
p.plot(back_targetAngles,  label='back target Angles')

p.legend()
p.show()

