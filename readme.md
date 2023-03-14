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

# Hypothesis

For this project, I attempted to test two hypothesis in order to see how the Robot will behave given different physical conditions.

## Hypothesis 1: Creatures with a smaller body part, aka links, will move farther than creatures with larger body parts. 

I predict this would be true as we often see in nature that living things with a larger limb/joints like Elephants or Giraffes cover less distance in comparison to creatures with smaller body parts like Zebras, Foxes, or Lions given the same number of body parts. I assume this has to do with the fact that often larger body parts limit movement due to their weight. In addition, larger body parts sometimes reduce flexibility, thus creatures with larger body parts won't be able to make sudden movements or be quick to react to incidents like creatures with smaller body parts.

## Result for Hypothesis 1:

## Hypothesis 2: Creatures with stronger neural pathway will move further. 

Creatures with stronger synaptic weight connection between  sensory neurons, hidden neurons, and motor neurons would move farther as they will be able to make quick and reactive movements given environmental stimulai. I predict this to be true because of the inter-dependence nature of neurons. The stronger the connection is between things, the more easie it is for information to flow between them. Thus, the presense of a stronger synaptic weight between neurons could lead to a more efficient motor neuron response which, in turn, would result in efficient locomotion. 


# Reference

This work takes inspiration from ludobots subreddit. www.reddit.com/ludobots.

