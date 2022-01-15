#Inspired by 3blue1brown, this generates a (5,11) Hamming code, simulates an error, and finds the error location
#This can definitely be optimized for more efficiency, but it works perfectly

#Note: I didn't watch the video until after I full worked it out myself, and then I felt silly for not doing it in less than 10 lines of code 

import random
bitSize = [0] * 16

#Displaying the Hamming code in a 4x4 chart
def display():
    newline = 0
    print()
    print(" ---------------------")
    for i in range(16):
        newline += 1
        if (newline == 4):
            #Create a new line
            print(" ", bitSize[i])
            print(" ---------------------")
            newline = 0
        else:
            #Print on same line
            print(" ", bitSize[i], " |", end = "")
    print()

print("Default configuration")
display()

for i in range(16):
    #Generating the data portion of hamming code
    if (i != 0):
        if (i != 1):
            if (i != 2):
                if (i != 4):
                    if (i != 8):
                        bitSize[i] = random.randrange(0, 2)
                    else:
                        bitSize[i] = 0
                else:
                    bitSize[i] = 0
            else:
                bitSize[i] = 0
        else:
            bitSize[i] = 0
    else:
        bitSize[i] = 0

print("Hamming code with just data")
display()
    
bitSize[0] = 1
for i in range(4):
    #Each index happens to be on exponents of 2
    bitSize[(2**i)] = 1

print("Hamming code with default parity added")
display()

#Parity (1) of index 1 - skipcount starting from 1 by 2
j = 1
temp = 0
for i in range(8):
    #print (bitSize[j], j)
    temp += bitSize[j]
    j += 2 #Skipcount by 2
    
parity = temp % 2
if (parity == 1):
    bitSize[1] = 0

print()
print("index 1:", parity, temp)

#Parity (2) of index 2 - skip first 2, count next 2 (x4)
j = 2
temp = 0
for i in range(4):
    for i in range(2):
        #print (bitSize[j], j)
        temp += bitSize[j]
        j += 1 #Count twice
    j += 2 #Skip first two of next line

parity = temp % 2
if (parity == 1):
    bitSize[2] = 0

print()
print("index 2:", parity, temp)

#Parity (3) of index 4 - skip first line, count next line (x2)
j = 4
temp = 0
for i in range(2):
    for i in range(4):
        #print (bitSize[j], j)
        temp += bitSize[j]
        j += 1 #Count four times
    j += 4 #Skip a row
    
parity = temp % 2
if (parity == 1):
    bitSize[4] = 0

print()
print("index 4:", parity, temp)

#Parity (4) of index 8 - count last half of array
j = 8
temp = 0
for i in range(8):
    #print (bitSize[j], j)
    temp += bitSize[j]
    j += 1 #Thankfully just a simple count
    
parity = temp % 2
if (parity == 1):
    bitSize[8] = 0

print()
print("index 8:", parity, temp)

#Parity (5) of index 0 - final countdown of everything to check for a double error
temp = 0
for i in range(16):
    #print (bitSize[i], i)
    temp += bitSize[i]

parity = temp % 2
if (parity == 1):
    bitSize[0] = 0

print()
print("index 0:", parity, temp)
print()
print()

#Final generated code
print("Hamming code with adjusted parity")
display()

print("Hamming code in array form")
print(bitSize)

##############################
##############################
##############################
##############################

#This section will be dedicated to inputing and computing an error
print()
print()
print("We shall now create an error in the data")
print("'0' Means that section is alright")
print("'1' Means that the parity had to be changed to make it even again, so the error is in that section")
print()

print("Choosing random bit...")
error = random.randrange(0, 16)
while (error == 0 or error == 1 or error == 2 or error == 4 or error == 8):
    print("Random bit picked was parity bit. Rechoosing for simplicity...")
    error = random.randrange(0, 16)

if (bitSize[error] == 0):
    bitSize[error] = 1
else:
    bitSize[error] = 0

print("Hamming code with an error somewhere...")
display()

#Now to find it

errorLocation = [0] * 4

#Index 1
j = 1
temp = 0
for i in range(8):
    #print (bitSize[j], j)
    temp += bitSize[j]
    j += 2 #Skipcount by 2
    
parity = temp % 2
print("Index 1:", parity)
errorLocation[0] = parity

#Index 2 
j = 2
temp = 0
for i in range(4):
    for i in range(2):
        #print (bitSize[j], j)
        temp += bitSize[j]
        j += 1 #Count twice
    j += 2 #Skip first two of next line

parity = temp % 2
print("Index 2:", parity)
errorLocation[1] = parity

#Index 4
j = 4
temp = 0
for i in range(2):
    for i in range(4):
        #print (bitSize[j], j)
        temp += bitSize[j]
        j += 1 #Count four times
    j += 4 #Skip a row
    
parity = temp % 2
print("Index 4:", parity)
errorLocation[2] = parity

#Index 8
j = 8
temp = 0
for i in range(8):
    #print (bitSize[j], j)
    temp += bitSize[j]
    j += 1 #Thankfully just a simple count
    
parity = temp % 2
print("Index 8:", parity)
errorLocation[3] = parity


print("The error location is ", end = "")
for i in range(4):
    print(errorLocation[i], end = "")
print()
print()

foundError = 0
for i in range(4):
    if (errorLocation[i] == 1):
        foundError += 2**(i)

print()
print("The program calculated the Binary to narrow the error down to index", foundError)
print("Value was held in seperate variable. The actual error is at index", error)


        
print()
print("Scroll back up to read it all!")
print("Or run it back if you don't believe the code can't work a second time!")
