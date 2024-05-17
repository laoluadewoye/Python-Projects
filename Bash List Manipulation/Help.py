"""
FUNCTIONS -

create - create new list (Null, A, B, C...cap at 26 lists)
    create {name} - creates new list with specified name
    
add {list} {value} - Add a value to specified list
    add - adds default value 0 to default list Null
    add {list} - adds default value 0 to specified list
    add -i {list} - adds default value 0 to specified index on specified list
    add -i {list} {value} - Add a value to specified index on specified list

display {letter} - print contents of specific list
    display - prints contents of all lists
    display -o - organizes everything
    
transfer - Adds value from the list after Null (typically A) to Null
    transfer (-o) {original list} - transfers last value of original to Null
    transfer (-ot) {original list} {target list} - transfers last value of original to target
    transfer (-oi) {original list} {index} - transfers specific value of original to Null
    transfer (-oti) {original list} {target list} {indexes}
        # like -ot, but you get to specify indexes of both original and target
    transfer (-t) {target list} - transfers last value of default list (typically A) to target
    transfer (-ti) {target list} {index} - transfers last value of default list to specific index of target

quit - quit program with Y or n. You can also technically press any key.

help - displays the main help menu.

clear - clears terminal screen. For viewing pleasure and ease.

trash - clear Null

"""


def mainHelp():
    print()
    print("'create' - create new list (Null, A, B, C...stops at 26 lists)")
    print("'create {name}' - creates new list with specified name")
    print("'create -h' - opens help menu for create command")
    print()
    print("'add' - adds default value 0 to default list Null")
    print("'add {list}' - adds default value 0 to specified list")
    print("'add -v {list}' - Add a value to specified list")
    print("'add -i {list}' - adds default value 0 to specified index on specified list")
    print("'add -i -v {list}' - Add a value to specified index on specified list")
    print("'add -h' - opens help menu for add command")
    print()
    print("'display' - prints contents of all lists")
    print("'display {list name}' - print contents of specific list")
    print("'display -o' - organizes list display")
    print("'display -h' - opens help menu for display command")
    print()
    print("'transfer' - Adds value 0 to Null from the list right after Null")
    print("'transfer -o' - Specify original list to pop a value off of")
    print("'transfer -t' - Specify target list to send value to")
    print("'transfer -i' - Specify the indexes you want to send or take from")
    print("'transfer -h' - Please review this for how to PROPERLY use transfer")
    print()
    print("'print' & 'print {letter}' - aliases for display commands")
    print()
    print("'quit' - quits program with Y or n. You can also technically press any key.")
    print()
    print("'popEnd {list}' - alias of transfer {original list}")
    print()
    print("'help' - displays the main help menu.")
    print()
    print("'clear' - clears terminal screen. For viewing pleasure and ease.")
    print()
    print("'trash' - clean Null list. Think of Null as a recycle bin.")
    print()
    print()


def createHelp():
    print()
    print("'create' - creates a new list for user to manipulate")
    print()
    print("# First is automatically named A and each new addition goes down the alphabet.")
    print("# It goes down until Z, then does not add anymore default lists.")
    print("# Any other list will have to be a custom name.")
    print()
    print("         ### Additional Info ###")
    print("-----------------------------------------------------------------------------")
    print("'create {name}' - creates new list with a custom name from the user.")
    print("# Is excluded from limitations of default-named lists.")
    print("# The name is treated as a string or character. Spaces and special characters are allowed.")
    print()
    print()


def displayHelp():
    print()
    print("'display' - displays all the lists created during the duration of the program.")
    print()
    print("# The lists will be displayed in a default way. The first item in each list is the name.")
    print()
    print("         ### Additional Info ###")
    print("-----------------------------------------------------------------------------")
    print("'display -o' - displays everything in an organized branching manner.")
    print("# Example:")
    print("#    examplelist")
    print("#        item 1, item 2, item 3...")
    print()
    print("'display {list name}' - displays the specific list user chooses.")
    print("#    Example is 'display A'.")
    print("# If the list does not exist, you won't get an output.")


def addHelp():
    print()
    print("'add' - Adds the default number 0 to the default list Null")
    print()
    print("# The basic version of add command if executed without arguments.")
    print("# Numbers are always added to the end of the list")
    print()
    print("         ### Additional Info ###")
    print("-----------------------------------------------------------------------------")
    print("'add {list}' - adds the default value of zero to a specified list by the user.")
    print("# With the -i (index) option, you can also specify where you want the zero in your list.")
    print("#    Example - \"add -i Null\"")
    print("# Name must match one of your lists.")
    print("# DO NOT PLACE ANYTHING AT INDEX ZERO.")
    print()
    print("'add -v {list}' - adds a specified value to a user-selected list.")
    print("# Now allows you to choose the value. Also supports -i option.")
    print("# Example - \"add -i -v Null\". You will then be asked to provide a value.")
    print("# Value must be a number.")
    print()
    print()


def transferHelp():
    print()
    print("'transfer' - takes the last value from one list and places it in another.")
    print("# The default list taken from is the one after Null. This would usually be the A list.")
    print("# The default target list is Null.")
    print("# The value will be deleted from the original list in the processes.")
    print()
    print("         ### Additional Info ###")
    print("-----------------------------------------------------------------------------")
    print("'-i' option - allows you to select the index you wish to use.")
    print("# Only really created for tandem use with other two options.")
    print("# Only use numbers with this option.")
    print()
    print("'-o' option - allows you to select the list you will pull a value from.")
    print("# Please write the correct name for a proper selection.")
    print()
    print("'-t' option - allows you to select the list you will send a value to.")
    print("# Same rules as the -o option.")
    print()
    print("# Options can be stacked on top of each other in any way possible.")
    print("#    i.e. transfer -oti")
    print("# You cannot use any other letters or characters, or else you will get an error.")
    print("# After you select the options you wish to use, you will then be able to put the actual parameters.")
    print()
    print()
