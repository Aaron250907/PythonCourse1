print('Variables in Python')
num = 23
print (num)

NUM = 45
print (NUM)

# This proves that Pyhon is Case Sensitive

# Different Ways to Declare Variables
num_1 = 1
num_first = 2
num1 = 3
num_ = 4
_num = 5
_ = 6

print(num_1)
print(num_first)
print(num1)
print(num_)
print(_num)
print(_)

# 1_num = Invalid Syntax
#num-1 = Invalid Syntax
#num*1 = Invalid Syntax

#Multiple Assignments With Different Values

x = y = z = 10
print(x)
print(y)
print(z)

#Multiple Variables With Same Values

a,b,c = 11,12,13
print(a)
print(b)
print(c)

print(a,b,c)

print(num, NUM, num_1, num_first, num1, num_, _num, _,x,y,z,a,b,c)

#Adition Using Variables
print(a+b)

# Examples of Multiple Mathematical Operations Using Variables
print(num + NUM - num_1 - num_first * num1 / num_ * _num + _ - x + y *z / a+b*c)

var_total = num + NUM - num_1 - num_first * num1 / num_ * _num + _ - x + y *z / a+b*c

# Using a text String as Variables Value
string1 = 'StemBirds'
print(string1)

string_1 = 'Sunday'
print('string_1')

# Example of Concatenation
var_1 = 'HTML'
var_2 = 'CSS'
var_3 = 'JS'
var_4 = 'Python'

print(var_1 + var_2 + var_3 + var_4)

var_5 = var_1 + var_2 + var_3
print(var_5)

print(type(var_total))
print(type(c))
print(type(var_5))

float1 = var_total
print(float1,type(float1))


# If the same name is given for variables with different values the last value will always be dsiplayed beacue the others wull be owerwrittten
d = 70
d = 80
d = 90

print(d)