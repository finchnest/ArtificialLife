How to start the creature:

    Run the 3dbody.py file.

Running 3dBody.py will result in a 3d creature in 3d space. To achieve this I did

- Create a random number of links between 5 and 10
- Then I added joints. #joints = #links - 1
- Then I randomly chose links to have sensors
- Then the Robot body was generated with randomly sized blocks at a random position around a previously positioned block. In other words, there were 8 directions to chose from for a given block.
- Then I connected each sensor to each motor by creating synapses. Thus all sensors and motors are connected. 
- Different kinds of body shapes are possible: like snakes or a randomly connected 3d creature. 

Example of joint connection of the creatures links are shown in the link below: https://github.com/finchnest/ArtificialLife/blob/assign7/IMG_0457.HEIC

