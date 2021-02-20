# Break Statement
# Finding out if 88 is present in the list given or not

List1 = [72,22,67,14,88,34,2,9,54,37,]

# Executing using For Loop

for i in List1 :
    print(i)
    if (i == 88):
        print("88 is present in List1")
        print("Terminate The Loop Immediately")
        break

# Execution using While Loop

x = 0
while x < 100 :
    print(List1[x])
    if (List1[x] == 88) :
        print("88 is present in List1")
        print("Terminate The Loop Immediately")
        break
    x =x +1

# Continue
# Find the Square of All the numbers in List2 except Number 79

List2 = [45,1,27,99,35,79,64,23,87,94]
for j in List2 :
    if (j == 79) :
        print("Blank *********")

        continue
    print("Square of", j, "=", j*j)

# Operation Using While Loop
a = 0
while a < 10 :
    if (List2[a] == 79):
        print("Blank *********")
        a = a+1
        continue
    print("Square of", List2[a], "=", List2[a]*List2[a])
    a= a + 1