import pyrosim.pyrosim as pyrosim


length = 1
width = 1
height = 1

# x = 0
# y = 0
# z = 0.5

x = 0
y = 0
z = 0.5

x2 = 0
y2 = 0
z2 = 0.5

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[2,y,z] , size=[length, width, height])
    pyrosim.End()
Create_World()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    #part 1
    
    pyrosim.Send_Cube(name="Link0", pos=[x,y,z] , size=[length, width, height])
    
    pyrosim.Send_Joint(name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1])

    pyrosim.Send_Cube(name="Link1", pos=[x,y,z] , size=[length, width, height])
    
    pyrosim.Send_Joint(name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [0,0,1])
    
    pyrosim.Send_Cube(name="Link2", pos=[0,0,0.5] , size=[length, width, height])

    pyrosim.Send_Joint(name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute", position = [0,0.5,0.5])
    
    pyrosim.Send_Cube(name="Link3", pos=[0,0.5,0] , size=[length, width, height])

    pyrosim.Send_Joint(name = "Link3_Link4" , parent= "Link3" , child = "Link4" , type = "revolute", position = [0,1,0])
    
    pyrosim.Send_Cube(name="Link4", pos=[0,0.5,0] , size=[length, width, height])

    pyrosim.End()
Create_Robot()

























# pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2] , size=[length, width, height])

# for i in range(10):
#     pyrosim.Send_Cube(name="Box"+str(i), pos=[x,y,z+i] , size=[length, width, height])
#     width = width * 0.9
#     length = length * 0.9

# for i in range (5):
#     for j in range (5):
#         for k in range (10):
#             pyrosim.Send_Cube(name="Box"+str(k), pos=[x+i,y+j,z+k] , size=[length, width, height])
#             width = width * 0.9
#             length = length * 0.9
#         width = 1
#         length = 1
#         j = j + 1
#     i = i + 1



