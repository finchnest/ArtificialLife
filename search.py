import os

from  hillclimber import HILL_CLIMBER
from parallelHIllClimber import PARALLEL_HILL_CLIMBER

# hc = HILL_CLIMBER()
# hc.Evolve()


phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()



# for x in range(5):
# 	os.system("python3 generate.py")
# 	os.system("python3 simulate.py")