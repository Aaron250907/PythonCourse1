# Differnet Operations On Lists

List1 = [
    11, 22, 33, 44, 55, 66, 77, 88, 99
]# List of Integers

print('List1 = ',List1 )

print('Lenght = ',len(List1))
#len is used to find the length of the Elements

List1.insert(2,100)
print('List 1 With Insert Function', List1)
# Insert Used to Insert Charcthers in Lists at PARTICULAR INDEX POSITION

List1.append(200)
print('List1 with Append Function', List1)
# Append Used only to add charcter at the END OF TTHE LIST

List1.remove(77)
print('List1 when used remove Function to remove 77 ', List1)
# Remove is used to REMOVE A CHRACTER

A = List1.pop(6)
# Saves the Index Value fo the Integer and the Text String from the list and saves in another Variable
print('List1 with the pop function', List1)
print(A)

List1.reverse()
print(List1)
# Reverse Reverses the Order of the List

small_value =  min(List1)
big_value = max(List1)

print('Minimum Value of List1 =',small_value)
print('Maximum Value of List1 = ', big_value)

# Inline Commands
print('Minimum Value of List1 =',min(List1))
print('Maximum Value of List1 =',max(List1))

List1.sort()
print(List1)
#Sort is used to SORT THE LIST IN ASCENDING ORDER

List2 = [20, 34, 58, 79, 65, 34]
List2.sort()
print(List2)
print(List2[0])
print(List2[-1])

print(List1)
print(List1[4:8])
print(List1[0:6])
print(List2[-4:-1])
#: Will Select Index From So and So
print(List2[1:])
# Prints From Index Value Till End of the List
print(List1[:5])
# Prints all index Values tii Index Value Written
print(List2[0:6:2])
# Select From index 0-5 at the Interval of 2

concat1 = [1,3,5,7,9]
concat2=[2,4,6,8,10]

concat3 =concat1 +concat2
print(concat3)

concat4 = concat1[1:3] + concat2[2:3]