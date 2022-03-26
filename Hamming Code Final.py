"""
    The final self-exercise in making a hamming unicode

    Today, I'm going to implement a RAID 0 concept called data striping on a large set of data

    6 bits can store a number up to 63

    So I'm going to generate a random amount of bits, then divide that into blocks of 63 bits per blocks

    Next, I'm going to have each block set its own parity check.

    Lastly, the blocks will place their data back into the set.
"""

from functools import reduce
import random
import numpy as np

import time


def delay():
    print("4 seconds till refresh")
    time.sleep(1)
    print("3 seconds till refresh")
    time.sleep(1)
    print("2 seconds till refresh")
    time.sleep(1)
    print("1 seconds till refresh")
    time.sleep(1)


# Function to call for each array.
def ParitySetup(bitSize):
    initError = reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bitSize) if bit])
    print("Index:", initError)

    # Turning that bit into binary form
    initErrorString = bin(initError)

    # Remove the '0b' label
    initErrorStringAdjusted = initErrorString.replace('0b', '')

    initErrorString = initErrorStringAdjusted

    initErrorStringFormatted = ''.join(reversed(initErrorString))

    # Adding the zeros
    while len(initErrorStringFormatted) < 6:
        initErrorStringFormatted = initErrorStringFormatted + '0'

    # Step 3: Don't forget to reverse it back to proper state
    initErrorStringReversed = initErrorStringFormatted
    initErrorString = ''.join(reversed(initErrorStringFormatted))

    print("Binary form:", initErrorString)

    return initErrorStringReversed


def PreparingArray(IESR, bitSize):  # Init Error String Reversed
    for i in range(len(IESR)):
        if IESR[i] == "1":
            if bitSize[2 ** i] == 1:
                bitSize[2 ** i] = 0
            else:
                bitSize[2 ** i] = 1
            print("Parity Bit", 2 ** i, "was flipped.")

    return bitSize


# First, create 8 default arrays
blockLength = 63

redundant1 = [0] * blockLength
redundant2 = [0] * blockLength
redundant3 = [0] * blockLength
redundant4 = [0] * blockLength
redundant5 = [0] * blockLength
redundant6 = [0] * blockLength
redundant7 = [0] * blockLength
redundant8 = [0] * blockLength

# second, list them in an array of their own

redundantBlocks = [redundant1, redundant2, redundant3, redundant4, redundant5, redundant6, redundant7, redundant8]

# third, generating the data
dataBank = np.random.randint(0, 2, random.randrange(0, 500))

# np.random.randint(0, 2, random.randrange(0, 500))

print(dataBank, end="\n\n")

dataBankLength = len(dataBank)

print("Number of bits:", dataBankLength)

# Configuring number of Arrays

numberOfArrays = dataBankLength // blockLength

idealLength = (numberOfArrays + 1) * blockLength

spillOverLength = idealLength - dataBankLength

print("Number of full blocks:", numberOfArrays)

print("Ideal number of bits:", idealLength)

print("Spillover bits:", spillOverLength)

print("\nPreparing to strip data. Please wait.")
delay()

# Copying data into arrays
print()
blockTick = 0
index = 0
for i in range(dataBankLength):
    redundantBlocks[blockTick][index] = dataBank[i]
    print("The value in index", index, "of array index", blockTick, "is", dataBank[i])
    time.sleep(0.05)
    blockTick += 1
    if blockTick == 8:
        blockTick = 0
        index += 1

print("\nPreparing to display samples. Please wait.")
delay()

print()
print("Sample of first array:  ", redundant1[0:6])
time.sleep(0.5)
print("Sample of second array: ", redundant2[0:6])
time.sleep(0.5)
print("Sample of third array:  ", redundant3[0:6])
time.sleep(0.5)
print("Sample of fourth array: ", redundant4[0:6])
time.sleep(0.5)
print("Sample of fifth array:  ", redundant5[0:6])
time.sleep(0.5)
print("Sample of sixth array:  ", redundant6[0:6])
time.sleep(0.5)
print("Sample of seventh array:", redundant7[0:6])
time.sleep(0.5)
print("Sample of eight array:  ", redundant8[0:6])
time.sleep(0.5)
print()
print("\nPreparing to prepare data parity. Please wait.")
delay()

print()
print()

# Preparing the blocks of data
print("Processing block 1...")
parityValues = ParitySetup(redundant1)
print("Sorting form:", parityValues)
redundant1 = PreparingArray(parityValues, redundant1)
print()
print()
time.sleep(1)

print("Processing block 2...")
parityValues = ParitySetup(redundant2)
print("Sorting form:", parityValues)
redundant2 = PreparingArray(parityValues, redundant2)
print()
print()
time.sleep(1)

print("Processing block 3...")
parityValues = ParitySetup(redundant3)
print("Sorting form:", parityValues)
redundant3 = PreparingArray(parityValues, redundant3)
print()
print()
time.sleep(1)

print("Processing block 4...")
parityValues = ParitySetup(redundant4)
print("Sorting form:", parityValues)
redundant4 = PreparingArray(parityValues, redundant4)
print()
print()
time.sleep(1)

print("Processing block 5...")
parityValues = ParitySetup(redundant5)
print("Sorting form:", parityValues)
redundant5 = PreparingArray(parityValues, redundant5)
print()
print()
time.sleep(1)

print("Processing block 6...")
parityValues = ParitySetup(redundant6)
print("Sorting form:", parityValues)
redundant6 = PreparingArray(parityValues, redundant6)
print()
print()
time.sleep(1)

print("Processing block 7...")
parityValues = ParitySetup(redundant7)
print("Sorting form:", parityValues)
redundant7 = PreparingArray(parityValues, redundant7)
print()
print()
time.sleep(1)

print("Processing block 8...")
parityValues = ParitySetup(redundant8)
print("Sorting form:", parityValues)
redundant8 = PreparingArray(parityValues, redundant8)
print()
print()

print("\nPreparing to return data to original storage. Please wait.")
delay()

# Putting block data back into original storage
print()
blockTick = 0
index = 0

for i in range(dataBankLength):
    dataBank[i] = redundantBlocks[blockTick][index]
    print("The bit", redundantBlocks[blockTick][index], "in index", index, "of block", blockTick,
          "is inserted into index", i, "of the storage.")
    time.sleep(0.05)
    blockTick += 1
    if blockTick == 8:
        index += 1
        blockTick = 0

print("\nPrinting updated data. Please wait.")
delay()

print()
print(dataBank)
