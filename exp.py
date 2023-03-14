import time

start = time.time()
while True:

    time.sleep(1)
    print(" under 5 ")
    if(time.time() - start > 5):
        print("finished")
        break

