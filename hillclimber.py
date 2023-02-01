

from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
            self.parent = SOLUTION()
    def Evolve(self):
        self.parent.Evaluate(GUI=True)

        for currentGeneration in range(c.NUMBER_OF_GENERATIONS):
            print()
            print("CASE-----> ", currentGeneration)
            self.Evolve_For_One_Generation()

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
