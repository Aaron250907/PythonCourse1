# Code for sum of all odd number from 1 to n

Number = int(input("Enter any Number : "))

if Number % 2 == 0 :
    print("Number is an even number");

else:
    print("Number is an odd number");
i = 1
while Number > i :
    i = i + 2
    print(i - 2)
    Sum = sum(range(1, Number, 2))
    if (Number == i-1):
        break

print("Sum = ", Sum)
