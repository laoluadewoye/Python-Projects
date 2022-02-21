#matrix calculator
#Date: 02/20/2022
#Author: Laolu Ade

def dataInput (row, column, length):
    matrix = [[]] * row #create rows 
    
    for i in range(row):
        matrix[i] = [0] * column #create columns in each row
    
    print("\n")
    
    for i in range(len(matrix)):
        print(f'row {i+1}\n', matrix[i], "\n") #Label of row in matrix
        
        for j in range(len(matrix[i])):
            matrix[i][j] = int(input("Please enter a number: ")) #For entering data in smallest indexes
            
    return matrix #Brings list data back to main program


print("Welcome to matrix calculator!")
print("You will be able to create two matrixes of any dimension and do multiplcation on them!")
print("Note - you will not be able to multiply a isSingle matrix by a number. Like, come on that's just basic math. Don't be lazy :/")
print("I mean, unless you want to be efficent (smart lazy). Kind of the point of python scripts I guess.")

isSingle = ''

while (isSingle != 'yes' and isSingle != 'no'):
    isSingle = input("\nDoooo you want to do a isSingle number against a matrix? (will repeat until you say yes/no)\n\n")

if (isSingle == 'yes'):
    print("\nAlright, lets do this!")
    #Entering paramater data
    try:
        numRowOne = int(input("How many rows in matrix 1? "))
        numColOne = int(input("How many columns in matrix 1? "))
        
        isSingleNumber = int(input("What number are you multiplying by? "))
    except ValueError:
        print("Please put a proper number. Must rerun program to continue.")
        quit()
    
    #Deciding the amount of indexes needed
    matrixOneDataAmount = numRowOne * numColOne
    
    print("\nEntering data for matrix one", end='')
    mtrx1 = dataInput(numRowOne, numColOne, matrixOneDataAmount)
    
    print("\nMatrix:")
    for i in range(len(mtrx1)):
        print(mtrx1[i])
        
    #COMPUTATION SECTION
    print("\nCreating output matrix")
    print("------------------------")
    for i in range (numRowOne):
        for j in range (numColOne):
            mtrx1[i][j] *= isSingleNumber
    
    #printing output
    for i in range(len(mtrx1)):
        print("   ", mtrx1[i])

elif (isSingle == 'no'):
    print("\nMultiplying two matrixes it is then.")
    
    #Entering paramater data
    try:
        numRowOne = int(input("How many rows in matrix 1? "))
        numColOne = int(input("How many columns in matrix 1? "))
        numRowTwo = int(input("\nHow many rows in matrix 2? "))
        numColTwo = int(input("How many columns in matrix 2? "))
    except ValueError:
        print("Please put a proper number. Must rerun program to continue.")
        quit()
    
    #Deciding the amount of indexes needed
    matrixOneDataAmount = numRowOne * numColOne 
    matrixTwoDataAmount = numRowTwo * numColTwo
    
    print("\nEntering data for matrix one", end='')
    mtrx1 = dataInput(numRowOne, numColOne, matrixOneDataAmount)
    
    print("\nEntering data for matrix two", end='')
    mtrx2 = dataInput(numRowTwo, numColTwo, matrixTwoDataAmount)
    
    print("\nFirst Matrix:")
    for i in range(len(mtrx1)):
        print(mtrx1[i])
        
    print("\nSecond Matrix:")
    for i in range(len(mtrx2)):
        print(mtrx2[i])
    
    print("\nCreating output matrix")
    print("------------------------")
    resultRows = numRowOne
    resultColumns = numColTwo
    
    resultMatrix = [[]] * resultRows 
        
    for i in range(resultRows):
        resultMatrix[i] = [0] * resultColumns
        
    #COMPUTATION SECTION
    temp = 0
    dotProduct = 0
    rowshift = 0
    columnshift = 0
    
    #READABLE EXAMPLE OF HOW COMPUTATION WILL WORK
    #example multiplies a 2 by 3 matrix (ONE) with a 3 by 2 matrix (TWO)
    
    # temp = 0
    # temp = temp + matrixOne[0][0] x matrixTwo[0][0] 
    # temp = temp + matrixOne[0][1] x matrixTwo[1][0] 
    # temp = temp + matrixOne[0][2] x matrixTwo[2][0]
    # dotProduct (in certain index) = temp
    # shift to next column in row of result
    
    # temp = 0
    # temp = temp + matrixOne[0][0] x matrixTwo[0][1] 
    # temp = temp + matrixOne[0][1] x matrixTwo[1][1] 
    # temp = temp + matrixOne[0][2] x matrixTwo[2][1]
    # dotProduct (in certain index) = temp
    # shift to next row of result
    
    # temp = 0
    # temp = temp + matrixOne[1][0] x matrixTwo[0][0] 
    # temp = temp + matrixOne[1][1] x matrixTwo[1][0] 
    # temp = temp + matrixOne[1][2] x matrixTwo[2][0]
    # dotProduct (in certain index) = temp
    # shift to next column in row of result
    
    # temp = 0
    # temp = temp + matrixOne[1][0] x matrixTwo[0][1] 
    # temp = temp + matrixOne[1][1] x matrixTwo[1][1] 
    # temp = temp + matrixOne[1][2] x matrixTwo[2][1]
    # dotProduct (in certain index) = temp
    
    for k in range(numRowOne): #For each row in the first matrix we are going to do math...
        for m in range(numColTwo): #On each column on the second matrix....
            for o in range(numColOne):
                #And multiply each number in the row of the first by each number in the column of the second.
                temp = temp + mtrx1[k][o] * mtrx2[o][m] #formula is same as above examples
            resultMatrix[rowshift][columnshift] = temp #Where dot Product is stored
            #print (resultMatrix[rowshift][columnshift]) - for if you want to see each number get printed
            columnshift += 1
            if (columnshift == resultColumns):
                columnshift = 0
            temp = 0
        rowshift += 1
        if (rowshift == resultRows):
            rowshift = 0
    
    #printing output
    for i in range(len(resultMatrix)):
        print("   ", resultMatrix[i])
        
    if (numColOne != numRowTwo):
        print("\nThis input did not satisfy one of the requirements for dot product multiplcation.")
        print("Result could be confusing and may not be accurate.")
