def newList(num, lists): #Creates a default new lsit
    lists.append([chr(num)]) #Converts the list number to a capital letter
    print (chr(num))
    num = num + 1 #increases number for next default name
    return num

def newListCustom(name, lists):
    isDefaultName = False
    for i in range(26): #Name check to make sure no default names are taken
        letter = chr(ord('A') + i)
        if (name == letter):
            print("You cannot use this name")
            isDefaultName = True
    if (isDefaultName == False):
        #Only runs if name is not default name
        lists.append([name])
        print(name)

def listCap(num): 
    if (num > ord('Z')): #Ensures only 26 default lists are made.
        print("No more default lists will be created.")
        return False
    else:
        return True
