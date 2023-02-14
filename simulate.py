import sys

from simulation import SIMULATION

directOrGUI = (sys.argv[1] == 'GUI')

solutionID = int(sys.argv[2])


simulation = SIMULATION(directOrGUI, solutionID)

simulation.Run()

# simulation.Get_Fitness()