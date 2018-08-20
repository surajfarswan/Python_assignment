# LIST

# Make list

l1 = []
n = int(input('Enter number of elemnets: '))
for i in range(0,n):
    a = input()
    l1.append(a)
print(l1)

# add following list to above list

l2 = ['google','apple','facebook','microsoft','tesla']
l3 = []
l3 = l1+l2
print(l3)

# count the number of times an object occurs in a list

a = []
n = int(input('Enter no. of elements: '))
for i in range(0,n):
    b = int(input())
    a.append(b)
print(a)
s = int(input('Enter no. to count: '))
print(a.count(s))

# create list with numbers and sort in ascending order

a = []
n = int(input('Enter no. of elements: '))
for i in range(0,n):
    b = input()
    a.append(b)
print(a)
a.sort()
print(a)

# given 2 arrays

a = [1,3,5,7]
b = [2,4,6,8]
c = []
c = a+b
c.sort()
print(c)

# count even and odd in list

l = []
c_even = 0
c_odd = 0
n = int(input('Enter no. of elements: '))
for i in range(0,n):
    a = int(input())
    l.append(a)
for i in l:
    if(i%2==0):
        c_even = c_even+1
    else:
        c_odd = c_odd+1
print('Number of even numbers: ',c_even)
print('Number of odd numbers: ',c_odd)

# TUPLES

# print tuple in reverse order
t = (1,2,3,4,5)
print(t[::-1])

# largest and smallest element in tuple
t = (1,2,3,4,5)
print('Maximum element: ',max(t))
print('Minimum element: ',min(t))

# STRINGS

# convert string to uppercase

string = input('Enter strig: ')
print(string.upper())

# print true if string contains all numeric characters

s = input('Enter string: ')
if (s.isnumeric()):
    print('True')
else:
    print('False')

# replace world with your name

st = "Hello World!"
print(st.replace('World','Trishali'))
