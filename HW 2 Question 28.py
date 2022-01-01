#Date: 09/17/21
#Name: Olaoluwa Adewoye
#Class: CTEC 125
#Code Description: This takes two numbers and does something that I can't
#                  decipher.


#import pythonlib 

#Deleted Declaration. No need for it in python

num1 = (eval(input("Enter first integer: ")))
num2 = (eval(input("Enter second integers: "))) #Optimized input 
 
if (num1 >= num2) and (num2 > 0): #Edited parentheses
    if num1 % num2 == 1: #Testing if the reminder of one and two is 1
        print("Reminder is 1")
        found = (num1 / num2 >= 6) #if one and two divided is higher than 6
                                   #Edited parentheses
        print("The first found is", found)
    elif (num1 == num1 / 2): #There was also a parentheses here
        print(num1, "=", num1, "divided by 2")
        quit() #Switched return to quit
    elif (num2 == num1 + num2): #Added proper comparison operator
        print(num2, "=", num1, "+", num2)
        quit() #Switched return to quit
    else: #Else was spelled wrong
        found = (2 * num2 < num1) #if 2 times num2 is less than one
        print("The secound found is", found)
    if (found):
        num2 = (eval(input("Enter a new second number: "))) #input needs to be properly input 
        num1 = num2 - num1 
        temp = (num1 + num2) / 10 
    elif (num2): #No need for semi-colon, only colon, changed to elif
        temp = num2 #temp needs to be declared as num2 there are no errors if found is False. 
        num1 = num2 
        num2 = temp #No need for colon
 
print (num1, " ", num2) #No need for plus signs, we use commas
