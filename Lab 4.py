average = 0
terminate = False
userInput = float(input("Please enter a number (negative numbers end the program): "))
    #kicks off program with first input
total = 1
minimum = userInput #There is only one number, so min and max are same
maximum = userInput
sum = userInput #there is only one number, so sum is same as input

if (userInput >= 0): #checks for negative number
    while (terminate != True): #infinite loop
        userInput = float(input("Enter another number: ")) #enters more numbers
        if (userInput < 0): #checks if negative number to end loop
            break
        total += 1 #adds to total of numbers
        sum += userInput #adds to sum of numbers
        if (userInput < minimum):
            minimum = userInput #checks if number is new lowest
        elif (userInput > maximum):
            maximum = userInput #checks if number is new highest
        average = sum / total #does math for average

    #prints everything when done
    print("Sum =", sum)
    print("average =", average)
    print("minimum =", minimum)
    print("maximum =", maximum)
else:
    print("Nothing is happening.") #Ends program without printing anything

print("End of Program.") 
