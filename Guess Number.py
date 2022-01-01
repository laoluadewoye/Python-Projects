num = 20

guess = eval(input("Guess the number: "))
if (guess == num):
    print("Congraduations, you guessed it.")
if (guess < num):
    print("No, it is a little higher than that.")
if (guess > num):
    print("No, it is a little lower than that.")
