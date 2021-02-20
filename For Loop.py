# For Loop

Numbers = [14, 78, 66, 32, 2, 4, 89]

for i in Numbers :
    print(i)

Sum = 0
for i in Numbers :
    Sum = Sum + i

print("Sum of all the numbers in ""Numbers = ", Sum)

NumberList2 = [2,5,3,7,9,4]

for i in NumberList2 :
    SquareRoot = i*i
    print("Square Root of the Numbers are = ", SquareRoot)

for r in range (1, 35) :
    # Range is an inbuilt function which will show value from the initial point to the second last number
    print(r)

for Number in range (1, 40):
    if (Number % 2) == 0 :
        print(Number)
        print("This is an Even number")

    else:
        print(Number)
        print("This is an Odd number")

print("This is the List of All the Odd and Even Numbers between 1 to 40")

for Range in range(1,21,2):
    print(Range)
    print("This is an Odd number")

for Range2 in range (2,21,2) :
    print(Range2)
    print("This is an Even number")

print("This is the List of All the Odd and Even Numbers between 1 to 20")

Table_No = int(input("Enter any number : "))
print("Table of ", Table_No)

for Count in range(1, 11) :
    print(Table_No, '*', Count,'=', Table_No * Count )


for x in range(1,5) :
    for y in range (20, 25):
        print(x, ' , ' , y)
