import sys

from simulation import SIMULATION

directOrGUI = (sys.argv[1] == 'GUI')

simulation = SIMULATION(directOrGUI)

simulation.Run()

simulation.Get_Fitness()