"""we are going to pick random chess squares"""

#First, make a list

chessSquare = [" "] * 64

convert = ord('a')

i = 0

fileMath = 0

while (i < 64):
    fileMath = (i + 1) % 8
    chessSquare[i] = str(chr(convert)) + str(fileMath)
    if (fileMath == 0):
        chessSquare[i] = str(chr(convert)) + str(8)
        convert += 1
    i = i + 1

print(chessSquare[:8])
print()

#Now we are going to make the actual chessboard

i = 0
counter = 0

while (counter < 8):
    print ("  ", chessSquare[i], "|", chessSquare[i+1], "|", \
           chessSquare[i+2], "|", chessSquare[i+3], "|", \
           chessSquare[i+4], "|", chessSquare[i+5], "|", \
           chessSquare[i+6], "|", chessSquare[i+7])
    if (counter < 7):
        print("   -------------------------------------")
    i += 8
    counter +=1

print()



            
