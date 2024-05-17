# I take one linux course and all of a sudden I'm formatting everything like a linux daemon

# command modules
import Quit
import Help
import Clear
import Create
import Display
import Add
import Transfer

# Start screen
print("Welcome to a code I made to mimic a linux bash to manipulate lists.")
print("Soon you will see a '>' to type after. This is where you will enter your commands.")
print("Type 'quit' to exit the program.")
print("Type 'help' for a list of commands to use.")
print("Type 'clear' to clear the screen.")
print()

mainList = [["Null"]]  # initialize the overall lists
command = ""  # initialize command

iterationName = ord('A')  # For created default named lists
moreLists = True  # Checking if any more default named lists can be made

keepRunning = True  # Keeps program running forever

while keepRunning:
    # input
    command = input("> ")

    # Checks for characters
    isChar = False
    for char in command:
        if 'a' <= char <= 'z':
            isChar = True

    ###Edge error cases###

    # blank input
    if command == '':
        print("You did not put anything.")

    # no lowercase letters (all commands are lowercase)
    elif not isChar:
        print("You typed an improper command.")

    ###Basic cases###

    # quit
    elif command == 'quit':
        keepRunning = Quit.quitprompt()

    # help
    elif command == 'help':
        Help.mainHelp()

    # clear
    elif command == 'clear':
        Clear.clearScreen()

    # trash
    elif command == 'trash':
        mainList[0] = ["Null"]
        print("Null list cleared")

    # LIST-SPECIFIC CASES

    # create command tree
    elif 'create' in command:
        # create
        if command == 'create':
            moreLists = Create.listCap(iterationName)
            if moreLists:
                iterationName = Create.newList(iterationName, mainList)
        else:
            commandParsed = command.replace("create ", "")
            commandParsed = commandParsed.strip()
            # create -h
            if commandParsed == "-h":
                Help.createHelp()
            # create {name}
            else:
                Create.newListCustom(commandParsed, mainList)

    # display command tree
    elif 'display' in command:
        # display
        if command == 'display':
            Display.showAll(mainList)
        else:
            commandParsed = command.replace("display ", "")
            commandParsed = commandParsed.strip()
            # display -h
            if commandParsed == "-h":
                Help.displayHelp()
            # display -o
            elif commandParsed == '-o':
                Display.showOrganized(mainList)
            # display {listname}
            else:
                Display.showSpecific(mainList, commandParsed)

    # add command tree
    elif 'add' in command:
        # add
        if command == 'add':
            Add.addList(mainList)
        else:
            commandParsed = command.replace("add ", "")
            commandParsed = commandParsed.strip()
            # add -h
            if commandParsed == "-h":
                Help.addHelp()

            ###add -i options###

            elif "-i" in commandParsed:
                commandOptionParsed = commandParsed.replace("-i ", "")
                commandOptionParsed = commandOptionParsed.strip()
                # add -i {list}
                if not ("-v" in commandOptionParsed):
                    try:
                        index = int(input("What index are you placing 0 in: "))
                        Add.add_Specific_List_Index(mainList, commandOptionParsed, index)
                    except (NameError, ValueError) as e:
                        print("Please use a proper number.")
                # add -i -v {list}
                else:
                    commandOptionParsed = commandOptionParsed.replace("-v ", "")
                    commandOptionParsed = commandOptionParsed.strip()
                    try:
                        index = int(input("What index do you choose: "))
                        value = input("What is the value you're inputing: ")
                        Add.add_i_v_options(mainList, commandOptionParsed, index, value)
                    except (NameError, ValueError) as e:
                        print("Please use a proper number.")
            # add -v {list}
            elif "-v" in commandParsed:
                commandOptionParsed = commandParsed.replace("-v ", "")
                commandOptionParsed = commandOptionParsed.strip()
                value = input("What is the value you're inputing: ")
                Add.add_Specific_List_Value(mainList, commandOptionParsed, value)
            # add {list}
            else:
                Add.add_Specific_List(mainList, commandParsed)

    # transfer command tree
    elif 'transfer' in command:
        # transfer
        if command == 'transfer':
            Transfer.move(mainList)
        else:
            commandParsed = command.replace("transfer ", "")
            commandParsed = commandParsed.strip()
            if '-' in commandParsed:
                # transfer -h
                if 'h' in commandParsed:
                    Help.transferHelp()
                else:
                    Transfer.moveOptionsMain(mainList, commandParsed)
            else:
                print("Improper transfer command syntax")

    # Default case
    else:
        print("Invalid command.")
