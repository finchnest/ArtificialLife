import os

from parallelHIllClimber import PARALLEL_HILL_CLIMBER
import matplotlib.pyplot as plt
import constants as c
import time
import numpy as np

os.system("python3 clean.py")        


trials = []

for conn_type, col in zip(['SELECTIVE', 'ALL'], ['green', 'blue']):
    
    best_fitnesses = []
    for x in range(1, 6):

        os.system("python3 clean.py")        
        time.sleep(2)

        print("------- Connection type {} Random Seed {} --------".format(conn_type, x))
        phc = PARALLEL_HILL_CLIMBER(conn_type)
        phc.Evolve()
        # phc.Show_Best()
        best_fitnesses.append(max(phc.best_creature_fitness))


        if x == 1:
            plt.plot([i + 1 for i in range(1, c.NUMBER_OF_GENERATIONS)], 
                    phc.best_creature_fitness, 
                    label="size {}".format(conn_type),
                    color = col)
        else:
            plt.plot([i + 1 for i in range(1, c.NUMBER_OF_GENERATIONS)], 
                    phc.best_creature_fitness, 
                    color = col)
       
    
    trials.append(best_fitnesses)

            
    # os.system("python3 clean.py")
    # time.sleep(5)


plt.title("Fitness of the best creature at each generation")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.legend()
plt.grid()
plt.savefig("Best_fitnesses.jpg")

for trial, ct in zip(trials, ['SELECTIVE', 'ALL']):
    print("STATS for connection type: {}".format(ct))
    print(trial)
    print("Mean: {}".format(np.mean(trial)))
    print("Max: {}".format(np.max(trial)))
    print("Std: {}".format(np.std(trial)))
    print("-----------------------")