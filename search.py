import os

from parallelHIllClimber import PARALLEL_HILL_CLIMBER
import matplotlib.pyplot as plt
import constants as c



for x in range(1, 5):

    print("Random Seed {}".format(x))
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    phc.Show_Best()

    plt.plot([i + 1 for i in range(c.NUMBER_OF_GENERATIONS)], 
             phc.best_creature_fitness, 
             label="random seed {}".format(x))

plt.title("Fitness of the best creature at each generation")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.legend()
plt.grid()
plt.savefig("Best_fitnesses.jpg")