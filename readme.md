______________________________  
###############################################################################\
###############################################################################\
#####################   CS_396: Artifical Life              \
#####################   Final Project By: Abenezer Tamene   \
#####################   THE SCIENCE OPTION                 \
###############################################################################\
###############################################################################
_____________________________


# How to start the creature:

    Run the search.py file.

# How it works

Running the program generates a creature with a random shape that is evolved to traval furtherest from its initial position. The fitness function favors creatures that travel farther. To achive this, synaptic weights of the creature's brain neuron are mutated.

# Body and Brain Generation

## Body generation

To create the body, a random number of links between 5 and 7 are generated. Then joints will be generated, i.e, #joints <= #links - 1. The links will have a random width, length, and height. Then based on a coin flip, a few links are chosen to have a sensor. The probability is fair. Following that links and joints are connected together. A given link has 1/8 chance of binding to one of the 8 corners of the 'previous' or parent link, since there are 8 corners. Details are attached below. Since links are attached in all the 3 directions with equal probability (+x, -x, +y, -y, +z, -z), infinitely many shapes are possible.  

![Plot](body_generation.jpg)

## Brain generation

For the brain, links that were assigned to have a sensors will be attached with a sensory neuron. Motors are added to all joints, however. Then a synaptic connection is made between sensory neurons and motor neurons. All sensory neurons will be connected to all motor neurons. 


# Mutation

The mutation chages synaptic weight  of neurons connection. If the connection results in a better fitness for a creature, the new connection will be chosen instead of the 'parent/previous' conection. 

# Selection

For the best creature selection, I used the algorithm described in parallelHillClimber.py. This works by first instantiating parent creatures. Then based on the number of generations set, each parent spawns a child with a different synaptic weight. Mutation causes change in synapse weight. Then the fitness of each mutated child is compared with its parent and if it's greater, the parent will be replaced with the child. Finally, fitness value of the best creature at each generatio is gathered and plotted.



# Hypothesis

For this project, I attempted to test two hypothesis in order to see how the Robot will behave given different physical conditions.

> Hypothesis 1: Creatures with stronger neural pathway will move further. 

Creatures with stronger synaptic weight connection between  sensory neurons, hidden neurons, and motor neurons would move farther as they will be able to make quick and reactive movements given environmental stimulai. I predict this to be true because of the inter-dependence nature of neurons. The stronger the connection is between things, the more easie it is for information to flow between them. Thus, the presense of a stronger synaptic weight between neurons could lead to a more efficient motor neuron response which, in turn, would result in efficient locomotion. 

>Hypothesis 2: Creatures with a smaller body part, aka links, will move farther than creatures with larger body parts. 

I predict this would be true as we often see in nature that living things with a larger limb/joints like Elephants or Giraffes cover less distance in comparison to creatures with smaller body parts like Zebras, Foxes, or Lions given the same number of body parts. I assume this has to do with the fact that often larger body parts limit movement due to their weight. In addition, larger body parts sometimes reduce flexibility, thus creatures with larger body parts won't be able to make sudden movements or be quick to react to incidents like creatures with smaller body parts.

# Methods

I wanted to test two hypothesis. One regarding the number of synaptic connection that there are in the creature and 2 the impact of body size. The measuring criteria was how far creatures moved from their initial position. For each hypothesis, I run 32,500 simulation totalling 65,000 simulations. In each hypothesis test, I run the simulation twice to see if their would be inconsistencies or changes due to random nature of size and shape generation. 

For Run 1, I run the simulation for 5 random seeds each with a population size of 5 and generation count of 250 for both SELECTIVE and ALL synaptic connection types totalling 12,500 simulation (2 types * 5 seeds * 5 population size * 250 generations = 12,500 sims)

For Run 2, I kept everything the same except for population size; I increased it to 8 resuling in 20,000 simulations (2 types * 5 seeds * 8 population size * 250 generations = 20,000 sims)

> Thus the total simulation done for hypothesis number 1 for both control and experimental groups is 32,500 simulations. For my computer, 2500 simulations took around 14 minutes. 

# Results and Discussion

## Result for Hypothesis 1:

> Fitness max, mean, and standard deviation for test on hypothesis 1. 
![Plot](selectiveVSall.png)

> Fitness graph for **Run 1**: simulation with a population size of 5
![Plot](run1Types.png)

> Fitness graph for **Run 2**: simulation with a population size of 8
![Plot](run2Types.png)

### **Discussion** 

The average fitness and the max fitness for creatures with more synaptic connection between neurons was higher than creatues with less neuron synaptic connection. This was inline with what I expected. In both Run 1 and Run 2, robots were able to move further when the number of neural connection in their brain was higher. The increase in the number of population for Run 2 resulted in a higher fitness which is expecpted since higher population size allows for various kinds of creatures which will, in turn, results in more diverse set of fitnesses. 

One interesting thing to note in both Run 1 and Run 2 is variation in standard deviation of fitness values. In both Runs, creatures with fully connected neural pathway showed a higher fitness value deviation from the mean. This implies that when there is a higher connection between neurons of a creatures, there is a good chance that a creature with a really high fitness value would appear at some point in the evolution. 

Lastly, I noted that in comparison to Run 1, creatures in Run 2 evolve more which makes sense as Run 2 has a higher population size per generaiton. It can be seen in the two fitness graphs above that Run 2 evolves more (fitness values keep increasing going upto 70) in comparison to Run 1 that doesn't evolve as much (max is capped around 60).



## Result for Hypothesis 2: 

> Fitness max, mean, and standard deviation for test on hypothesis 2. 
![Plot](size4VSsize05.png)

> Fitness graph for **Run 1**: simulation with a population size of 5
![Plot](run1Sizes.png)

> Fitness graph for **Run 2**: simulation with a population size of 8
![Plot](run2Sizes.png)


### **Discussion**

>Size in this test refers to a sclar that multiplies randomly generated size values which are between 0 and 1. 

For Run 1 with a population size of 5, the average fitness of creatures with size 4 was higher than creatures with a size of 0.5. This is contrary to what I expected. I expected creatures with smaller body parts would travel farther but according to the simulation, the opposite is true. One reason for this would be the lunge/step that larger creatures would take is higher than those will smaller steps. The maximum fitness value, however, is larger for creatures with a size of 0.5. I believe this could be due to the random nature of size and body shape generation as it's not seen for Run 2.

For Run 2 with a population size of 8, a similar pattern was seen like Run 1 interms of mean fitness value: creatures with larger size travelled farther by a significant margin. Again this confirms that creatures with a larger size could take advange of their bigger body parts to make bigger strides. 

I could not make a significant generalization about the standard deviation for each of the two Runs as what I found out was opposite for each case. Standard deviation was higher in Run 1 and maximum value was higher in Run 2.

Regarding the graph, I noticed the result was a bit from what I found out for hypothesis 1. In hypothesis 2, the graph shows more evolution (consistent increases) for Run 1 (the one with 5 population size) in comparison to Run 2 (the one with 8 population size). In fact, in one of the seeds for Run 2 (shown in black in the figure above), the fitness value remains constant throught the 250 generations. One of the reasons for this could be the possibilitiy that the highest fitness value was achieved early on due to randomness/luck and the generations that came after it have a lower or equal fitness value.


## Limitations and Future Work

The biggest source of uncertainity in my experiment was limitation of computing resource. I am running these simulations in a computer with 8GB RAM and 1.8GHz speed. This significantly afftected how many simulations I could have done. Even though I did a total of 65,000 simulations, running these simulations in a bigger and more efficient servers would have allowed me to see more interesting behaviors and patterns of locomotion. 

For this project I focused on locomotion aspect of creaures. Even though locomotion is important, there are wide variety of behaviors a creature can exhibit to survive like vision, sound detection, weight of the creature, types of joints between links, shape of body parts, etc. The environment could also be changed like the gravity, frictional value of the ground, etc. Investigating these behaviros would allow us simulate how livining things would have been affected in early stages of life. 


# Reference

This work takes inspiration from ludobots subreddit. www.reddit.com/r/ludobots.


