# # Reverse the list
l1 = []
n = int(input('Enter number of elemnets: '))
for i in range(0,n):
    a = input()
    l1.append(a)
l1.reverse()
print(l1)

# # Print all uppercase letters from a string

Str = input('Enter string: ')
for i in Str:
    if i>= "A" and i<="Z":
        print(i,end=" ")

# # Split the user input on comma's and store the values in a list as integers.

a = input('Enter string: ')
b = a.split()
print(','.join(b))

# # Pallindromic String or not

Str = input('Enter string: ')
Str1 = reversed(Str)
if list(Str) == list(Str1):
    print('Pallindromic String.')
else:
    print('Not a pallindromic string.')

# # Make deepcopy of list and write d/w b/w shallow and deep copy

import copy as cp
l1 = [1,2,3,[4,5,6]]
l2 = cp.deepcopy(l1)
l1[3][1]='Heya'
print(l1)
print(l2)


# In shallow copy, a reference object is copied in other object. In this changes made to a copy of object reflect in original object.It is done using "copy()" function.
# In deep copy, a copy of object is copied in other object. In this changes made to a copy of object doesn't reflect the original object. It is done using "deepcopy()" function.
