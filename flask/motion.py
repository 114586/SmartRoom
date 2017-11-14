import time
import threading

#global aan
global aan
aan = False

x = 0
e = threading.Event() # de functie threading.Event() wordt aangeroepen met e
while not e.wait(5): #
    print("motion waiting...")
    if aan:
        x += 1
        print("motion on", x)

def setOn():
    aan = True

def setOff():
    aan = False
