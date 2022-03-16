def move(lists): #Easist as it's default
    temp = lists[1][-1] #Always take from last index of list A
    lists[1].pop()
    lists[0].append(temp) #Add to end of Null list
    print("The value", temp, "was moved to Null")

def originalOption(lists, index): #Created as a template to save space
    originalList = input("What is the list you are pulling from: ")
    if (index != -1): #default index check
        try:
            index = int(input("What is the index you are taking from: "))
        except (NameError, ValueError, UnboundLocalError) as e:
            print("Incorrect input. Using default inputs. Results may be skewed.")
            index = -1
            temp = 0
    for iterlist in lists:
        if (iterlist[0] == originalList):
            temp = iterlist[index]
            iterlist.pop(index)
            print("value", temp, "was removed from list", iterlist[0], "from index", index)
    return temp
    
def targetOption(lists, value, index): #Created as a template to save space
    targetList = input("What is the list you're sending to: ")
    if (index != -1): #default index check
        try:
            index = int(input("What is the index you are sending to: "))
        except (NameError, ValueError, UnboundLocalError) as e:
            print("Incorrect input. Using default index.")
            index = -1
    for iterlist in lists:
        if (iterlist[0] == targetList):
            iterlist.insert(index, value)
            print("value", value, "was put into list", iterlist[0], "at index", index)

def moveOptionsTree(lists, optionInput):
    if ("o" in optionInput and "t" in optionInput): #indexes needed for possibly both
        if ("i" in optionInput): #indexes needed. Get all three
            value = originalOption(lists, 1)
            targetOption(lists, value, 1)
        else: #no index needed. Get original list and target list
            value = originalOption(lists, -1)
            targetOption(lists, value, -1)
    else: #only one index possibly needed
        if ("i" in optionInput): #index needed. need option for just 'i' alone
            if (optionInput == "-i"): #indexes only for some reason...
                print("i option cannot be used alone.")
                print("Well theroretically it could, but why would you care about something sent to Null?")
            elif ("o" in optionInput): #orignal list included. o and i
                value = originalOption(lists, 1)
                lists[0].append(value)
            elif ("t" in optionInput): #target list included. o and t
                try:
                    value = lists[1][-1]
                    lists[1].pop()
                    targetOption(lists, value, 1)
                except IndexError:
                    print("Add more data, there is literally no point right now.")
        else: #no index needed.
            if ("o" in optionInput): #original list only
                value = originalOption(lists, -1)
                lists[0].append(value)
            elif ("t" in optionInput): #target list only
                try:
                    value = lists[1][-1]
                    lists[1].pop()
                    targetOption(lists, value, -1)
                except IndexError:
                    print("Add more data, there is literally no point right now.")

def optionsCheck(optint):
    properOptions = False
    
    #erasing options in seperate variable
    leftover = optint.replace("-", "")
    leftover = leftover.replace("o", "")
    leftover = leftover.replace("t", "")
    leftover = leftover.replace("i", "")
    leftover = leftover.strip()
    
    if (leftover == ""): #A valid options section would be blank by now
        properOptions = True
    else: 
        print("incorrect syntax.")
    
    return properOptions
    
def moveOptionsMain(lists, optionInput):
    isValid = optionsCheck(optionInput) #Runs a small check to validate command
    
    if (isValid == True): #If true, goes into the options tree to find the proper output
        moveOptionsTree(lists, optionInput)
