

from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0



        for par in range(c.populationSize):
            self.parents[par] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        os.system("rm brain*.nndf")
        os.system("rm fitness*.nndf")


    def Evolve(self):
        
         
        self.Evaluate(self.parents)

        for currentGeneration in range(c.NUMBER_OF_GENERATIONS):
            print()
            print("Generation-----> ", currentGeneration)
            self.Evolve_For_One_Generation()
        self.Show_Best()


    def Evaluate(self,solutions, GUI = False):
        

        for parent in solutions:
            solutions[parent].Start_Simulation(GUI)

        for parent in solutions:
            solutions[parent].Wait_For_Simulation_To_End()
     
    def Evolve_For_One_Generation(self):

       
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Show_Best(self):

        self.max_key = next(iter(self.parents))
        self.min_key = next(iter(self.parents))

        for key in self.parents:
            if self.parents[key].fitness > self.parents[self.max_key].fitness:
                self.max_key = key
            if self.parents[key].fitness < self.parents[self.min_key].fitness:
                self.min_key = key

        print("highest fit: ", self.parents[self.max_key].fitness, " lowest fit: ", self.parents[self.min_key].fitness)

        self.parents[self.max_key].Start_Simulation(GUI=True)

    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID +=1            

    def Mutate(self):
        for parent in self.parents:
            self.children[parent].Mutate()

    def Select(self):
        for parent in self.parents:
            if self.parents[parent].fitness < self.children[parent].fitness :
                self.parents[parent] = self.children[parent]
    def Print(self):
        print()

        # print("pre_parent: ",self.parents[0].fitness, "pre_child: ", self.children[0].fitness)

        for (k,v), (k2,v2) in zip(self.parents.items(), self.children.items()):

            print("parent: ",v.fitness, "child: ", v2.fitness)


        print()