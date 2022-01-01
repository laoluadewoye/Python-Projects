print("Please put the entire name in lowercase")
print()

userString = input("Enter the first name: ")
userString2 = input("Enter the second name: ")
sum = 0
sum2 = 0

for i in range(0, len(userString)):
    sum += (ord(userString[i]) - 96)
for i in range(len(userString2)):
    sum2 += (ord(userString2[i]) - 96)

print("First name has value of", sum)
print("Second name has value of", sum2)
print()

compatability = sum + sum2

if (compatability > 120):
    compatability = compatability // 2

print("These two are", compatability, "% compatible")



