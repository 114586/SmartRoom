import time

x = 0
while True: #
    print("motion waiting...")
    #read data from file 
    #if file data = 1, aan = true
    file = open("Communicate_motion", "r")
    aan = int(file.read())
    if aan == 1:
        x += 1
        print("motion on", x)
    time.sleep(5)

