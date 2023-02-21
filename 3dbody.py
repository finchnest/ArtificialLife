from solution import SOLUTION

import os
import time


for i in range(1):
    sol = SOLUTION(i)
    sol.Start_Simulation(True)

    # while  os.path.exists("brain{}.nndf".format(i - 1)):
    #         time.sleep(0.01)
