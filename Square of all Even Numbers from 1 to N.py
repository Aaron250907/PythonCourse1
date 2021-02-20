# Code for Square of all even Numbers between 1 to N

Number = int(input("Enter Any Number : "))

print("Number = ",Number)
if Number % 2 == 0 :
    print("Number is an even number");

else:
    print("Number is an odd number");


for i in range (0,Number,2) :
    print("Square Root of", i, "=", i*i)
    i = i+1
