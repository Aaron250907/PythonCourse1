# Unit Converter

while(1) :
    print("\n 1. m - cm \n 2. km - m \n 3. g - kg \n 4. kg - g \n 5. l - ml \n 6. ml - l \n 7. Exit")
    Choice = int(input("Enter Your Choice = "))

    if Choice == 1 :
        M = int(input("Enter Unit : ",))
        CM = M * 100
        print(M, "m converted into cm = ",CM, "cm")

    elif Choice == 2 :
        KM = int(input("Enter Unit : "))
        M = KM * 1000
        print(KM, "km converted into m = ", M, "m")

    elif Choice == 3 :
         Gm = int(input("Enter Unit : "))
         KG = Gm / 1000
         print(Gm, "g converted into kg = ", KG, "kg")

    elif Choice == 4 :
        KG = int(input("Enter Unit : "))
        Gm = KG * 1000
        print(KG, "kg converted into g = ", Gm, "g")

    elif Choice == 5 :
        L = int(input("Enter Unit : "))
        ML = L * 1000
        print(L, "l converted into ml = ", ML, "ml"  )

    elif Choice == 6 :
         ML = int(input("Enter Unit : "))
         L = ML / 1000
         print(ML, "l converted into l = ", L, "l")

    elif Choice == 7 :
        print("Thank You")
        break

    else :
        print('Please Select A Valid Option')