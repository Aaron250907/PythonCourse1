# Area Calculation for Different Figures With Menu Driven Program

print("Select A Geometrical Figure of which you want to calculate the area")

while(1) :    # While(1) is an infinite loop. Also called as Forever Loop
    print("\n 1. Square \n 2.Rectangle \n 3.Circle \n 4.Triangle \n 5.Exit")
    Choice = int(input("Enter Your Choice = "))

    if Choice == 1 :
        Square_Lenght = int(input("Enter The Lenght  of the side of the Square : "))
        Result_Square = Square_Lenght*Square_Lenght
        print("Area of the Square = ",Result_Square,)

    elif Choice == 2 :
        Rect_Lenght = int(input("Enter The Lenght of the Rectangle : "))
        Rect_Breadth = int(input("Enter The Breadth of the Rectangle : "))
        Result_Rect  = Rect_Lenght*Rect_Breadth
        print("Are of The Rectangle = ",Result_Rect)

    elif Choice == 3  :
        Radius = int(input("Enter The Radius of the Circle : "))
        Result_Circle =  3.14 * Radius * Radius
        print("Area of Circle = ", Result_Circle)

    elif Choice == 4 :
        Height_Triangle = int(input("Enter Height of the Triangle : "))
        Base_Triangle = int(input("Enter The Base of the Triangle : "))
        Result_Triangle = Height_Triangle*Base_Triangle
        print("Area of the Triangle = ",Result_Triangle)

    elif Choice == 5:
        break

    else:
        print("Enter A Valid Choice")

print("Thank You for using the Area Calculator App")