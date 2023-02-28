# How to start the creature:

    Run the search.py file.

# How it works

Running the program generates a creature with a random shape that is evolved to traval furtherest from its initial position. The fitness function favors creatures that travel farther. To achive this, synaptic weights of the creature's brain neuron are mutated.

# Body and Brain Generation

## Body generation

To create the body, a random number of links between 5 and 7 are generated. Then joints will be generated, i.e, #joints <= #links - 1. The links will have a random width, length, and height. Then based on a coin flip, a few links are chosen to have a sensor. The probability is fair. Following that links and joints are connected together. For a given link, it has 1/8 chance of binding to the 'previous' or parent link, since there are 8 corners. Details are attached below. 

![Plot](body_generation.jpg)

## Brain generation

For the brain, links that were assigned to have a sensors will be attached with a sensory neuron. Motor is added to all joints, however. Then a synaptic connection is made between sensory neurons and motor neurons. All sensory neurons will be connected to all motor neurons. 


# Mutation

The mutation chages synaptic weight  of neurons connection. If the connection results in a better fitness for a creature, the new connection will be chosen instead of the 'parent/previous' conection. 

# Reference

This work takes inspiration from ludobots subreddit. www.reddit.com/ludobots.

