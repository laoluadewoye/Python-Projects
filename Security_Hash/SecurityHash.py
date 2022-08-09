def hashShifts(length):
    # Create shifts
    modZero = [1, 3, 5, 7, 8, 9, 2, 4, 6]
    modOne = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    modTwo = [2, 4, 6, 8, 1, 3, 5, 7, 9]
    modThree = [3, 6, 9, 2, 5, 8, 1, 4, 7]
    modFour = [4, 8, 3, 7, 2, 6, 1, 5, 9]
    modFive = [5, 9, 4, 8, 3, 7, 2, 6, 1]
    modSix = [6, 2, 8, 4, 1, 7, 5, 9, 3]
    modSeven = [7, 4, 1, 8, 5, 2, 9, 6, 3]
    modEight = [1, 3, 5, 9, 8, 6, 4, 2, 7]
    modNine = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    if length % 10 == 0:
        return modZero
    elif length % 10 == 1:
        return modOne
    elif length % 10 == 2:
        return modTwo
    elif length % 10 == 3:
        return modThree
    elif length % 10 == 4:
        return modFour
    elif length % 10 == 5:
        return modFive
    elif length % 10 == 6:
        return modSix
    elif length % 10 == 7:
        return modSeven
    elif length % 10 == 8:
        return modEight
    elif length % 10 == 9:
        return modNine


def hashGenerator(key):
    # Goal, create controlled randomness

    # Declaration
    hashNum = 0
    keyLength = len(key)

    # Choosing today's shifter. Will use these to scramble values
    modShift = hashShifts(len(key))

    for i in range(len(modShift)):
        modShift[i] = modShift[i] * len(key) + (modShift[0] * (-1**i))

    # ASCII Addition
    for i in range(len(key)):
        # Multiplies ASCII value by a number at modulated index of ASCII value
        hashNum += ord(key[i]) * modShift[(i % 9)]

    # Multiply and add by key length
    hashNum *= keyLength

    return hashNum


def hashOutput(numKey):
    modShift = hashShifts(numKey)

    characters = ""
    tickDown = numKey

    #Key Generation
    while len(characters) < 94:

        #Number countdown
        while tickDown > 254:
            tempTick = tickDown
            tempTick //= modShift[tickDown % 8 + 1]
            if tempTick == tickDown:  # Logic tree to prevent eternal loop
                tempTick -= 1  # Allows for new ModShift
                tickDown = tempTick
            else:
                tickDown = tempTick
            print(tickDown, end=", ")

        characters += hex(tickDown)[2:] + ","  # Add new hexadecimal
        charLength = len(characters)
        tickDown = (tickDown**(charLength % 4)) * tickDown  # Raise variable for another round

    print()

    return characters


phrase = input("Please enter any phrase as your key: ")
print("Key:", phrase)

number = abs(hashGenerator(phrase))
print("Number Hash:", number, end="\n\n")

hexa = hashOutput(number)
print(hexa)

hexaList = hexa.split(",")
print(hexaList)

hexaString = ""

for hd in hexaList:
    hexaString += hd

print("\nTrue Hash:", hexaString)


