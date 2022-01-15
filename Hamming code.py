import random

#This file will simulate a (5, 11) Hamming code.

def codedisplay():
    print()
    print(" ", parityFinal, " | ", parity[0], " | ", parity[1], " | ", information[0])
    print(" ---------------------")
    print(" ", parity[2], " | ", information[0], " | ", information[1], " | ", information[3])
    print(" ---------------------")
    print(" ", parity[3], " | ", information[4], " | ", information[5], " | ", information[6])
    print(" ---------------------")
    print(" ", information[7],  " | ", information[8], " | ", information[9], " | ", information[10])
    print()

def errorfinder():
    
    for i in range(8):
        

information = [1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0]

parity = [0, 1, 0, 0]

parityFinal = 1

print("Hamming code")
codedisplay()

biterror = random.randrange(0, 11)
if (information[biterror] == 1):
    information[biterror] = 0
else:
    information[biterror] = 1

print()
print("Hamming code with error")
codedisplay()
