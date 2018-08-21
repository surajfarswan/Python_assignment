## DECISION AND FLOW CONTROL

# Take input year and decide whether leap year or not

i = int(input('Enter year: '))
if i % 4 == 0:
    if i % 100 == 0:
        if i % 400 == 0:
            print(i,' is a leap year')
        else:
            print(i,'is not a leap year')
    else:
        print(i,' is a leap year')
else:
    print(i,' is not a leap year')

# Take length and breadth input from user and check whether the dimensions are of square or rectangle. 

l = int(input('Enter length: '))
b = int(input('Enter breadth: '))
if l == b:
    print('It is a square.')
else:
    print('It is a rectangle.')

# Take the input age of 3 people and determine oldest and youngest among them.

p1 = int(input('Enter age of person 1: '))
p2 = int(input('Enter age of person 2: '))
p3 = int(input('Enter age of person 3: '))
if p1>p2 and p1>p3:
    print('Person 1 is oldest')
    if p2>p3:
        print('Person 3 is youngest')
    else:
        print('Person 2 is youngest')    
elif p2>p1 and p2>p3:
    print('Person 2 is oldest')
    if p1>p3:
        print('Person 3 is youngest')
    else:
        print('Person 1 is youngest')        
elif p3>p1 and p3>p2:
    print('Person 3 is oldest')
    if p1>p2:
        print('Person 2 is youngest')
    else:
        print('Person 1 is youngest')
else:
    print('All are equal')

# Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.

age = int(input('Enter age: '))
sex = input('Enter sex M or F: ')
marital = input('Enter marital status Y or N: ')
if sex == 'F' or sex == 'f' and age >= 20 and age<=60:
    print("She'll work in urban areas.")
if sex == 'M' or sex == 'm':
    if age < 40 and age >=20:
        print('He may work anywhere.')
    if age < 60 and age>=40:
        print("He'll work in urban areas only.")
else:
    print('ERROR')

# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user. 
    
n = int(input('Enter quantity: '))
if n>1000:
    print('Total cost is: ',((n*100)-(0.1*n*100)))
else:
    print('Total cost is: ',(n*100))

## LOOPS

# Take 10 integers from user and print it on screen

n = []
for i in range(0,10):
    a = int(input())
    n.append(a)
print(n)

# Write an infinite loop.An infinite loop never ends. Condition is always true.

num = True
while num > 0:
    print(num)

# Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.

l = []
l1 = []
n = int(input('Enter no. of elements: '))
for i in range(0,n):
    a = int(input())
    b = a*a
    l.append(a)
    l1.append(b)
print('Original list: ',l)
print('Square of previous list: ',l1)

# From a list containing ints, strings and floats, make three lists to store them separately

l = [1,2,3,'abc','x',3.2,5.6]
Int = []
Str = []
Float = []
for i in range(0,len(l)):
    if isinstance(l[i],int):
        Int.append(l[i])
    elif isinstance(l[i],str):
        Str.append(l[i])
    else:
        Float.append(l[i])
print(Int)
print(Str)
print(Float)

# Using range(1,101), make a list containing only prime numbers. 

l = []
for i in range(1,101):
    j = 2
    c = 0
    while j<=i:
        if i%j ==0:
            c += 1
        j += 1
    if c > 1:
        continue
    else:
        l.append(i)
print(l)

# Print the following patterns:

i = 1
while i<=4:
    print ("*"*i)
    i = i+1

# Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop. 

l = []
n = int(input('Enter no. of elements: '))
for i in range(0,n):
    a = int(input())
    l.append(a)
print(l)
b = int(input('Enter element to delete: '))
if b in l:
    l.remove(b)
    print(l)
else:
    print("Element doesn't exist in list.")
    print(l)
    
