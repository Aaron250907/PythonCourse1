# ATM Machine
print("Welcome to the ATM")
print("Select Operation. 1.Widthraw, 2.Deposit and 3. Exit ")
Number1 = int(input('Enter your selection: '))
while(1) :
    if Number1 > 3 :
        print("Please Select A Valid Option \n")
        Number1 = int(input('Enter your selection: '))

    elif Number1 < 1:
        print("Please Select A Valid Option \n")
        Number1 = int(input('Enter your selection: '))

    elif Number1 == 3:
        print("Exiting")
        break

    else:
        Balance = 18000

    if Number1 == 1:
        print("\nBalance = ",Balance)
        Widthraw_amount_number = int(input("How much would you like to widthraw 1.500, 2.1000, 3.2000, 4.2500, 5.5000, 6.10000, 7.15000, 8.20000, 9. Other Amount : "))


        if Widthraw_amount_number == 1:
            if Balance < 500 :
                print("Insufficient Balance. Please Withdraw a Smaller Ammount")
            else:
                Balance = Balance - 500
                print("Balance =", Balance)

        if Widthraw_amount_number == 2:
            if Balance < 1000:
                print("Insufficient Balance. Please Withdraw a Smaller Ammount")
            else:
                Balance = Balance - 1000
                print("Balance =", Balance)

        if Widthraw_amount_number == 3:
            if Balance < 2000:
                print("Insufficient Balance. Please Withdraw a Smaller Ammount")
            else:
                Balance = Balance - 2000
                print("Balance =", Balance)

        if Widthraw_amount_number == 4:
            if Balance < 2500:
                print("Insufficient Balance. Please Withdraw a Smaller Ammount")
            else:
                Balance = Balance - 2500
                print("Balance =", Balance)

        if Widthraw_amount_number == 5:
            if Balance < 5000:
                print("Insufficient Balance. Please Withdraw a Smaller Ammount")
            else:
                Balance = Balance - 5000
                print("Balance =", Balance)

        if Widthraw_amount_number == 6:
            if Balance < 10000:
                print("Insufficient Balance. Please Withdraw a Smaller Ammount")
            else:
                Balance = Balance - 10000
                print("Balance =", Balance)

        if Widthraw_amount_number == 7:
            if Balance < 15000:
                print("Insufficient Balance. Please Withdraw a Smaller Ammount")
            else:
                Balance = Balance - 15000
                print("Balance =", Balance)

        if Widthraw_amount_number == 8:
            if Balance < 20000:
                print("Insufficient Balance. Please Withdraw a Smaller Ammount")
            else:
                Balance = Balance - 20000
                print("Balance =", Balance)

        if Widthraw_amount_number == 9:
            Other_Widthrawal_Amount = int(input("Please Enter Your Amount : "))
            if Other_Widthrawal_Amount > Balance :
                print("Insufficient Balance. Please Withdraw a smaller amount.")
                if Other_Widthrawal_Amount < 20000 :
                    print("You cannot widthraw an amount greater than 20000")

            else:
                Balance = Balance - Other_Widthrawal_Amount
                print("Balance =", Balance)

    elif Number1 == 2 :
        print("Balance = ",Balance)
        Deposit_amount_number = int(input("How much would you like to deposit 1.500, 2.1000, 3.2000, 4.2500, 5.5000, 6.10000, 7.15000, 8. Other Amount : "))
        if Deposit_amount_number == 1 :
            print("Your new Balance = ",Balance + 500)

        if Deposit_amount_number == 2 :
            print("Your new Balance = ",Balance + 1000)

        if Deposit_amount_number == 3 :
            print("Your new Balance = ",Balance + 1500)

        if Deposit_amount_number == 4 :
            print("Your new Balance = ",Balance + 2000)

        if Deposit_amount_number == 5 :
            print("Your new Balance = ",Balance + 5000)

        if Deposit_amount_number == 6 :
            print("Your new Balance = ",Balance + 10000)

        if Deposit_amount_number == 7 :
            print("Your new Balance = ",Balance + 15000)

        if Deposit_amount_number == 8 :
            Other_Deposit_Amount = int(input("Please Enter Your amount : "))
            print("Your new Balance = ",Balance + Other_Deposit_Amount)
