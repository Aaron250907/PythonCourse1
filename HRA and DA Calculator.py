#To input basic salary of an employee and calculate its Gross salary according to following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80% Basic Salary <= 20000 : HRA = 30%, DA = 90% Basic Salary > 20000 : HRA = 35%, DA = 95%

Salary = int(input("Enter Your Salary ₹ : "))
HRA = 0
DA = 0

if Salary <= 10000 :
    HRA = Salary * 20 / 100
    DA = Salary * 80 / 100
    GrossSalary = Salary+HRA+DA
    print("Gross Salary = ",GrossSalary)
    print("HRA = ", HRA)
    print("DA = ", DA)

elif Salary <= 20000 :
    HRA = Salary * 30 / 100
    DA = Salary * 90 / 100
    GrossSalary = Salary + HRA + DA
    print("Gross Salary = ", GrossSalary)
    print("HRA = ", HRA)
    print("DA = ", DA)

elif Salary >20000 :
    HRA = Salary * 35 / 100
    DA = Salary * 95 / 100
    GrossSalary = Salary + HRA + DA
    print("Gross Salary = ", GrossSalary)
    print("HRA = ", HRA)
    print("DA = ", DA)
