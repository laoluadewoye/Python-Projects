#Inspired by 3blue1brown, this generates a (255, 247) Hamming code, simulates an error, and finds the error location
#This this was optimized using the 3blue1brown strategy, except preparing the randomly generated code has been automated
#A great upgrade from (15, 11)


import random
from functools import reduce
import numpy as np
import time

#Time delay
def delay():
    print()
    print("Next step...")
    time.sleep(1)
    print("4 seconds till refresh")
    time.sleep(1)
    print("3 seconds till refresh")
    time.sleep(1)
    print("2 seconds till refresh")
    time.sleep(1)
    print("1 seconds till refresh")
    time.sleep(1)
    

#Displaying the Hamming code in a 16x16 chart
def display():
    newline = 0
    print()
    print(" ----------------------------------------------------------------------------------------------")
    for i in range(256):
        newline += 1
        if (newline == 16):
            #Create a new line
            print(" ", bitSize[i])
            print(" ----------------------------------------------------------------------------------------------")
            newline = 0
        else:
            #Print on same line
            print(" ", bitSize[i], " |", end = "")
            time.sleep(0.005)
    print()
    delay()

#Creates array of 1s and 0s    
bitSize = np.random.randint(0, 2, 256)

print("Randomly generated bits")
display()

#Function that carrots all bits that are set to 1 to find the initial error bit.
#lambda calls the xor carrot function, the code in brackets sifts through each bit to find the ones that are on
initError = reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bitSize) if bit])

#The resulting bit that gets output by the series of carrots
print("Index:", initError)
print()

#Turning that bit into binary form
initErrorString = bin(initError)


#Formatting the binary form
#-----------------------------------

#Step 1: Remove the '0b' label
initErrorStringAdjusted = initErrorString.replace('0b', '')

initErrorString = initErrorStringAdjusted

print(initErrorString)

#Step 2: Reverse string to add the zeros needed to make the string 8 bits
initErrorStringFormatted = ''.join(reversed(initErrorString))

print(initErrorStringFormatted)

#Adding the zeros
while (len(initErrorStringFormatted) < 8):
    initErrorStringFormatted = initErrorStringFormatted + '0'
    
print(initErrorStringFormatted)

#Step 3: Don't forget to reverse it back to proper state
initErrorStringReversed = initErrorStringFormatted
initErrorString = ''.join(reversed(initErrorStringFormatted))

print()
print("Binary form:", initErrorString)

#Keep the reversed version for the establishing of parity
print()
print("Establishing parity:")
print()
for i in range(len(initErrorStringReversed)):
    if (initErrorStringReversed[i] == "1"):
        bitSize[2**i] = not bitSize[2**i]
        print("Parity Bit", 2**i, "was flipped.")
 
initError = reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bitSize) if bit])

#The resulting bit that gets output by the series of carrots
print()
print("Updated Index Check:", initError)
if (initError == 0):
    print("Random code is now well prepared. Displaying new code.")
    display()

##############################
##############################
##############################
##############################

#This section will be dedicated to inputing and computing an error
print()
print()
print("We shall now create an error in the data")

print()

print("Choosing random bit...")
error = random.randrange(0, 256)
bitSize[error] = not bitSize[error]
print("Displaying code with one bit wrong.")
display()

foundError = reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bitSize) if bit])

print()
print("The program calculated the Binary to narrow the error down to index", foundError)
print("Value was held in seperate variable. The actual error is at index", error)

print()
print("Scroll back up to read it all!")
print("Or run it back if you don't believe the code can't work a second time!")
