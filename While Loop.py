# While Loop

Number = 0
while Number <=10 : # If the Condition is true, enter the Loop
    print(Number)
    Number = Number+2

print("Out of the Loop") # Whenever Condition is False


# Finding out all Odd Numbers from 1 - 10
i = 1
while i <= 10:
    print(i)
    i =  i+2

print("Out of the Loop")

# While Else
Number2 = 10
while Number2 >5 :
    print(Number2)
    Number2 = Number2 - 1

else:
    print(Number2, "is now less than 6")

# Nested While Loops

x = 1
while x < 3 :
    y = 5
    while y <= 8 :
        print(x, y)
        y = y + 1
    x = x + 1