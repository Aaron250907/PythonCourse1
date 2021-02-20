# Recursive Functions : When a function calls itself, the functions is knowm aa Recursive Functions

# To find Factorial of the Number with a recursive function

def Factorial(Number1):
    if Number1 == 1 :
        return 1

    else:
        return (Number1*Factorial(Number1-1))

Number2 = int(input("Enter any number : "))
print(Factorial(Number2))

'''
Program starts from int(input))

'''