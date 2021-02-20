# Functions in Python

# Function without Return Value

# def is a python keyword which indicates the starting of the function
#print_function is the name of the function
# String1 is the name of the argument

def print_function (): # Function is without Argument and Return Value
    print("Welcome to the Function")

print_function()   # Calling the Function

def print_function_with_argument (String1): # Function is with Argument and  without Return Value
    print(String1 + " Welcome to the Function")

print_function_with_argument('Aaron')
print_function_with_argument('Buzz')

def multi_string(String1, String2):
    print('The current day is', String1, 'and the current month is', String2)

multi_string('Sunday', 'Feburary')

def multi_string_default(String1, String2 = 'Feburary'):
    print('The current day is', String1, 'and the current month is', String2)

multi_string_default('Sunday')
multi_string_default('Sunday', 'March')

#Addition of two numbers with functions

def add(Number1, Number2): # This Function is with Return Function. It will return the addition of numbers
    return Number1+Number2
ResultAddition = add(10, 20) # Calling a function as part of the Mathematical Equation

print("Sum of 10 and 20 = ",ResultAddition)
#print(Number1) # Will give an error as the scope of Number1 and Number2 is only in the function

#Result = add(100, 200)
print("New Result is",add(100, 200))

#add() This will give an error

#Subtraction with default argument

def subtraction(Number1 = 0, Number2 = 0) :
    return Number1-Number2

ResultSubtraction1 =  subtraction(30,10)
ResultSubtraction2 = subtraction(30)
ResultSubtraction3 = subtraction()
ResultSubtraction4 = subtraction(Number2=20)

print(ResultSubtraction1)
print(ResultSubtraction2)
print(ResultSubtraction3)
print(ResultSubtraction4)