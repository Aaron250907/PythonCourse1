# Code for Squre of all even Numbers between 1 to N Using While Loop

Number = int(input("Enter ny Number : "))

print("Number = ",Number)
if Number % 2 == 0 :
    print("Number is an even number");

else:
    print("Number is an odd number");

a = 0
while a < Number :
    a = a+2
    print("Square of", a, "=", a*a)


