def addList(lists):  # default
    lists[0].append(0)
    print("Value", 0, "was added to the list", lists[0][0])


def add_Specific_List(lists, listChoice):
    for iterlist in lists:
        if iterlist[0] == listChoice:  # Choose a list to add to
            iterlist.append(0)
            print("Value", 0, "was added to list", iterlist[0])


def add_Specific_List_Index(lists, listChoice, index):
    for iterlist in lists:
        if iterlist[0] == listChoice:  # Choose a list and index to add to
            iterlist.insert(index, 0)
            print("Value", 0, "was added to list", iterlist[0], "at index", index)


def add_i_v_options(lists, listChoice, index, value):
    for iterlist in lists:
        if iterlist[0] == listChoice:  # Chose a list, index, and value to add
            iterlist.insert(index, value)
            print("Value", value, "was added to list", iterlist[0], "at index", index)


def add_Specific_List_Value(lists, listChoice, value):
    for iterlist in lists:
        if iterlist[0] == listChoice:  # Chose a list and value to add
            iterlist.append(value)
            print("Value", value, "was added to list", iterlist[0])
