import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[4,y,z] , size=[length, width, height])
    pyrosim.End()
Create_World()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")



    pyrosim.Send_Cube(name="Link0", pos=[1.5, 0, 2.5], size=[length, width, height])
    
    pyrosim.Send_Joint(name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position =  [1,0,2])

    pyrosim.Send_Cube(name="Link1", pos= [-0.5, 0, -0.5] , size=[length, width, height])
    

    pyrosim.Send_Joint(name = "Link0_Link2" , parent= "Link0" , child = "Link2" , type = "revolute", position = [2, 0, 2])
    
    pyrosim.Send_Cube(name="Link2", pos=[0.5, 0, -0.5] , size=[length, width, height])




    pyrosim.End()
Create_Robot()
