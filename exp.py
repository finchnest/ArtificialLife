import time
import os
import random
start = time.time()
import numpy as np
# while True:

#     time.sleep(1)
#     print(" under 5 ")
#     if(time.time() - start > 5):
#         print("finished")
#         break

for x in range (10):
    l = [random.random(), random.random(), random.random()] 
    # l = [x * 3 for x in l]

    print(l)

# ar = []
# ar.append(1)
# ar.append(-2)
# ar.append(5)
# ar.append(0)

# print(ar[-1])
# print(max(ar))

# fn = "fit_folder/fitness" + str(0) + ".txt"

# print(os.stat(fn).st_size == 0)

# print(3 % 3 == 0 or 6%4 == 0)

# f = open('testvv.txt','w')
# f.write("STATS for link size: {}".format(1))
# x = [1,2,3]
# f.write(str(x))
# f.write("Mean: {}".format(np.mean(x)))
# f.write("Max: {}".format(np.max(x)))
# f.write("Std: {}".format(np.std(x)))
# f.write("-----------------------")
# f.close()