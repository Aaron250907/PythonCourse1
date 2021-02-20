# Decsion Making
data1 = input ('Enter any Data :')
print(data1)
print(type(data1))
#  By Default while Entering data using the input function and afterwards checking the type, the Class will always show as STRING

print(data1 + 10)
# You cannot do mathematical operations on a string
data2 = int(input('Enter Any Data:'))
print(data2)
print(type(data2))
print(data2 + 10)

# int(input()is used to convert a string of numbers to type int

#If Statement

flag = True # Compulasry to put Capital T#
if flag == True :
   print('Today is Sunday')

flag = False
if flag == True:
   print('This is A Python Session')

data3 = int(input('Enter any Number :' ))
if data3 <10 :
    print('Number Entered is less than 10')
    print('Out of Loop')

# If & Else Statements
data4 = int(input("Enter any Number : "))
if data4 < 10 :
     print('Number Entered is Less Than 10')
else:
     print('Number Entered is More Than 10')
     print("Out of If Condition")

# If Elif Else

data5 = int(input("Enter Any Number : "))
if data5 <10 :
      print("Number is Less Than 10")
      print("Inside If")

elif data5 > 10 :
      print("Number is Greater Than 10")
      print("Inside Elif")

else:
      print("Number is = 10")
      print("Inside Else")

print("Out of Loop")
# Task :  take two numbers from user and compare

a = int(input("Enter Any Number :- "))
b = int(input("Enter Any Number :- "))
if a < b :
     print(a, "is" ,"<" ,b)
elif a > b :
    print(a, "is" ,">" ,b)
else:
    print(a, "is" ,"=" ,b)
print("Result is displayed above")

# HW = Take marks for 5 subjects. calculate the %.  then give the grade





