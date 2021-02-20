# HW = Take marks for 5 subjects. calculate the %.  then give the grade
Sub1 = int(input("Enter The Marks :- "))
Sub2 = int(input("Enter The Marks :- "))
Sub3 = int(input("Enter The Marks :- "))
Sub4 = int(input("Enter The Marks :- "))
Sub5 = int(input("Enter The Marks :- "))

List_marks = [Sub1,Sub2,Sub3,Sub4,Sub5]

print("Subject 1 : ", Sub1)
print("Subject 2 : ", Sub2)
print("Subject 3 : ", Sub3)
print("Subject 4 : ", Sub4)
print("Subject 5 : ", Sub5)

print(List_marks)
total_marks_of_user = sum(List_marks)
print("The Total Marks are :- ",total_marks_of_user)

total = int(input("Enter The Total No.Marks :- "))

percent = total_marks_of_user / total * 100

if percent >= 90:
    print("A Grade")
    print("Wonderful")

elif percent >= 80  :
    print("B Grade")
    print("You have Done Well")

elif percent >= 70:
    print("C Grade")
    print("You have Done Well")

elif percent >= 60:
    print("D Grade")
    print("Good Try")

elif percent >=50 :
    print("Pass Grade")
    print("Good Try")

else:
    print("F Grade")
    print("You have Failes")
print(percent,"%")


