

from solution import SOLUTION
import constants as c
import copy
import os

class HILL_CLIMBER:
    def __init__(self):

        os.system("rm brain*.nndf")
        os.system("rm fitness*.nndf")
        self.id = 1
        self.parent = SOLUTION(self.id)
       
    def Evolve(self):
        self.parent.Evaluate(GUI=False)

        for currentGeneration in range(c.NUMBER_OF_GENERATIONS):
            print()
            print("Generation-----> ", currentGeneration)
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(GUI=False)

        # self.Select()

        self.Print()


    def Show_Best(self):
        self.parent.Evaluate(GUI=True)
        self.child.Evaluate(GUI=True)

        print("parent fit: ", self.parent.fitness, " child fit: ", self.child.fitness)
        
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
    

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness < self.child.fitness :
            self.parent = self.child
    def Print(self):
        print()
        print("parent_fitness: ", self.parent.fitness, " child_fitness: ",self.child.fitness)
        print()
