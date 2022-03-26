def quitprompt():
    quitChoice = input("Do you want to quit? (Y/n)\n> ")
    if quitChoice == 'Y':
        no_exit = False
    elif quitChoice == 'n':
        no_exit = True
    else:
        print("please choose Y or n next time.")
        no_exit = True
    return no_exit
