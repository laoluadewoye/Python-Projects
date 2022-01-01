"""Program will take 10 numbers greater than from user
   add them to list variable
   prints entire list of numbers
   and prints list of only the even numbers in list."""

#Greater than 0 check function
def numCheck(num):
    while (num <= 0): #Will keep repeating until number greater than 0 is entered
        num = int(input("Try again! Enter another number: "))
    return int(num)



#Start of Program
numbers = [] #Making empty list

for i in range(10): #i counts up to 10 for 10 numbers
    userIn = int(input("Please enter a number greater than 0: "))
    userIn = numCheck(userIn) #Checks number first
    numbers.append(userIn) #Then adds it to the list

print () #Spacing
print ("All numbers:", numbers) #Prints out the list

print ("Even numbers: ", end = "") #Prints out the beginning of even numbers

for i in range(len(numbers)):
    evenCheck = numbers[i] % 2 #Uses the remainder to find even numbers
    if (evenCheck == 0):
        print(numbers[i], end = ", ") #Keeps numbers on the same line

print () #Spacing
print ()
print ("End of program.")
