

from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self, conn_type):
        self.parents = {}
        self.nextAvailableID = 0
        self.best_creature_fitness = []

        for par in range(c.populationSize):
            self.parents[par] = SOLUTION(self.nextAvailableID, conn_type)
            self.nextAvailableID += 1

        # os.system("rm brain*.nndf")
        # os.system("rm body*.urdf")
        # os.system("rm fitness*.txt")


    def Evolve(self):
        
        print("Generation-----> ", 1)

        self.Evaluate(self.parents)

        for currentGeneration in range(2, c.NUMBER_OF_GENERATIONS + 1):
            print()
            print("Generation-----> ", currentGeneration)
            self.Evolve_For_One_Generation()


    def Evaluate(self,solutions, GUI = False):
        

        for parent in solutions:
            solutions[parent].Start_Simulation(GUI)

        for parent in solutions:
            solutions[parent].Wait_For_Simulation_To_End()
     
    def Evolve_For_One_Generation(self):

       
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        # self.Print()
        self.Select()

    def Show_Best(self):
        
        best_parent = self.parents[0]
        for parent in self.parents.values():
            if parent.fitness < best_parent.fitness:
                best_parent = parent

        print("highest fit: ", best_parent.fitness)
        best_parent.Start_Simulation(GUI=True)
        best_parent.Wait_For_Simulation_To_End()


    def Spawn(self):
        self.children = {}
        for p_id in self.parents:
            self.children[p_id] = copy.deepcopy(self.parents[p_id])
            self.children[p_id].Set_ID(self.nextAvailableID)
            self.nextAvailableID +=1            

    def Mutate(self):
        for child in self.children.values():
            child.Mutate()

    def Select(self):
        bcf = -1
        for p_id in self.parents:
            if self.parents[p_id].fitness < self.children[p_id].fitness :
                self.parents[p_id] = self.children[p_id]
            bcf = max(self.parents[p_id].fitness, bcf)
        self.best_creature_fitness.append(bcf)
            
    def Print(self):
        print()
        for index in self.parents.keys():
            print("child fitness: {}, parent fitness: {}".format(self.children[index].fitness, self.parents[index].fitness))