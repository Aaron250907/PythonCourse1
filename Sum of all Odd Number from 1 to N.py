# Code for sum of all odd number from 1 to n

Number = int(input("Enter any Number : "))

if Number % 2 == 0 :
    print("Number is an even number");

else:
    print("Number is an odd number");

for i in range(1, Number, 2) :
    print(i)
    Sum = sum(range(1, Number, 2))
print("Sum = ", Sum)
