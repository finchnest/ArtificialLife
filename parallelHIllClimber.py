

from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
            self.parents = {}
            self.nextAvailableID = 0

            for par in range(c.populationSize):
                self.parents[par] = SOLUTION(self.nextAvailableID)
                self.nextAvailableID += 1



    def Evolve(self):
        for parent in self.parents:
            self.parents[parent].Start_Simulation(GUI = True)

        for parent in self.parents:
            self.parents[parent].Wait_For_Simulation_To_End()

    def xEvolve(self):
        pass

        # for currentGeneration in range(c.NUMBER_OF_GENERATIONS):
        #     print()
        #     print("CASE-----> ", currentGeneration)
        #     self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(GUI=False)

        self.Select()

        self.Print()


    def Show_Best(self):
        self.parent.Evaluate(GUI=True)
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
    

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness < self.child.fitness :
            self.parent = self.child
    def Print(self):
        print("<------>")
        print("parent fitness is ", self.parent.fitness, " and child fitness ",self.child.fitness)
        print("<------>")
