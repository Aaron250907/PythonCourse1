# Factorial Using For Loop

Number = int(input("Enter Any Number : "))
factorial = 1

for f in range (1, Number + 1) :
    factorial = factorial * f
print("Factorial of", Number, "=", factorial)
