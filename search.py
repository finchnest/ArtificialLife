import os

from  hillclimber import HILL_CLIMBER
from parallelHIllClimber import PARALLEL_HILL_CLIMBER

# hc = HILL_CLIMBER()
# hc.Evolve()
# hc.Show_Best()


phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()

