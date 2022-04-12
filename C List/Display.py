def showAll(lists):
    print(lists)  # Display list as it's default format


def showSpecific(lists, choice):
    for iterlist in lists:
        if iterlist[0] == choice:  # Choose specific list to show
            print(iterlist)
            break


def showOrganized(lists):  # Display list in organized way
    print()
    for iterlist in lists:
        print(iterlist[0], "\n\t", end="")  # Print the name of list

        for i in range(1, len(iterlist)):  # Print the values of the list
            print(iterlist[i], end=", ")
        print(" ")
