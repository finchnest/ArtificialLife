import os

from parallelHIllClimber import PARALLEL_HILL_CLIMBER
import matplotlib.pyplot as plt
import constants as c
import time
import numpy as np

os.system("python3 clean.py")        

for op in range(2):
    if op == 0:
        trials = []

        for conn_type, col in zip(['SELECTIVE', 'ALL'], ['green', 'blue']):
            
            best_fitnesses = []
            for x in range(1, 6):

                os.system("python3 clean.py")        
                time.sleep(2)

                print("------- Connection type {} Random Seed {} --------".format(conn_type, x))
                phc = PARALLEL_HILL_CLIMBER(conntion_type = conn_type)
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


        plt.title("Fitness of the best creature at each generation for synapse test")
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.legend()
        plt.grid()
        plt.savefig("Best_fitnesses_synapse_test.jpg")

        for trial, ct in zip(trials, ['SELECTIVE', 'ALL']):
            

            f = open('hypo_test_connection_type.txt','w')
            f.write("STATS for connection type: {}".format(ct))
            f.write(str(trial))
            f.write("Mean: {}".format(np.mean(trial)))
            f.write("Max: {}".format(np.max(trial)))
            f.write("Std: {}".format(np.std(trial)))
            f.write("-----------------------")
            f.close()

    else:
        trials = []

        for size, col in zip([0.5, 4], ['pink', 'green']):
            
            best_fitnesses = []
            for x in range(1, 6):

                os.system("python3 clean.py")        
                time.sleep(2)

                print("------- Size {} Random Seed {} --------".format(size, x))
                phc = PARALLEL_HILL_CLIMBER(size_adjust = size)
                phc.Evolve()
                # phc.Show_Best()
                best_fitnesses.append(max(phc.best_creature_fitness))


                if x == 1:
                    plt.plot([i + 1 for i in range(1, c.NUMBER_OF_GENERATIONS)], 
                            phc.best_creature_fitness, 
                            label="size {}".format(size),
                            color = col)
                else:
                    plt.plot([i + 1 for i in range(1, c.NUMBER_OF_GENERATIONS)], 
                            phc.best_creature_fitness, 
                            color = col)
            
            
            trials.append(best_fitnesses)

                    
            # os.system("python3 clean.py")
            # time.sleep(5)


        plt.title("Fitness of the best creature at each generation for link size")
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.legend()
        plt.grid()
        plt.savefig("Best_fitnesses_link_size.jpg")

        for trial, size in zip(trials, [0.5, 4]):
            f = open('hypo_test_link_size.txt','w')
            f.write("STATS for link size: {}".format(size))
            f.write(str(trial))
            f.write("Mean: {}".format(np.mean(trial)))
            f.write("Max: {}".format(np.max(trial)))
            f.write("Std: {}".format(np.std(trial)))
            f.write("-----------------------")
            f.close()