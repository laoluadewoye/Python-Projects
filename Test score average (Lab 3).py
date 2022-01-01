#Program will take three test scores from user, and print the output along
    #with the letter grade
#Date: 09/30/21
#Name: Olaoluwa Adewoye

testScore1, testScore2, testScore3 = eval(input("Please enter three test scores separated by commas: "))
#User enters the scores in a tuple form

aveScore = (testScore1 + testScore2 + testScore3) / 3
print("Your average score is", aveScore, ".")
#Calculates Average Score

if (aveScore >= 90): #Range for an A grade
    print("Your letter Grade is A.")
elif (aveScore >= 80): #Range for an B grade
    print("Your letter Grade is B.")
elif (aveScore >= 70): #Range for an C grade
    print("Your letter Grade is C.")
elif (aveScore >= 60): #Range for an D grade
    print("Your letter Grade is D.")
else: #Everything under 60 is an E
    print("Your letter Grade is E.")

print()
print("End of Program.")
