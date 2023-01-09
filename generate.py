import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

x2 = 0
y2 = 1
z2 = 1.5
# pyrosim.Send_Cube(name="Box1", pos=[x,y,z] , size=[length, width, height])
# pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2] , size=[length, width, height])

# for i in range(10):
#     pyrosim.Send_Cube(name="Box"+str(i), pos=[x,y,z+i] , size=[length, width, height])
#     width = width * 0.9
#     length = length * 0.9

for i in range (5):
    for j in range (5):
        for k in range (10):
            pyrosim.Send_Cube(name="Box"+str(k), pos=[x+i,y+j,z+k] , size=[length, width, height])
            width = width * 0.9
            length = length * 0.9
        width = 1
        length = 1
        j = j + 1
    i = i + 1


pyrosim.End()

