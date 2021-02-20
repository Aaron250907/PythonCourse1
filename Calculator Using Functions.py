#rewrite the project calculator  with the help of funtion
# Menu Based Calculator to perform addition, subtraction, multiplication & division

print("Welcome to my calculator")

Number1 = int(input('Enter the 1st Number : '))
Number2 = int(input('Enter the 2nd Number : '))

while(1) :
    print("\n Select Operation")
    print(" 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Square \n 6.Exit")
    Choice = int(input("Select Your Opeartion : 1(Addition), 2(Subtraction), 3(Multipliction), 4(Division, 5(Sqaure) and 6(Exit) : "))

    if Choice == 1 :
        Result = Number1 + Number2
        print(Number1, "+", Number2, "=" ,Result)

    elif Choice ==2 :
        Result = Number1 - Number2
        print(Number1, "-", Number2, "=", Result)

    elif Choice ==3 :
        Result = Number1 * Number2
        print(Number1, "x", Number2, "=",  Result)

    elif Choice ==4 :
        Result = Number1 / Number2
        print(Number1, "/", Number2, '=',  Result)

    elif Choice == 5:
        Result = Number1*Number1
        Result1 = Number2*Number2
        print("Square of", Number1, "=", Result)
        print("Square of", Number2, "=", Result1)

    else:
        print("Please Select a Valid Option")
        break

def add():
    Number1+Number2
    print('Sum')