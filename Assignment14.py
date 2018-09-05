## LIST COMPREHENSION & GENERATOR EXPRESSION

# Question 1

n = int(input('Enter no. of elements: '))
l = [i*i*i for i in range(0,n)]
print(l)

# Question 2

m = int(input('Enter starting range: '))
n = int(input('Enter ending range: '))
l = [x for x in range(m,n) if 0 not in [x%i for i in range(2,int(x/2)+1)]]
print(l)

# Question 3

# Generator Expression: It returns the object and object can be iterated over.It is enclosed in plain parantheses().In this we can't access the element by index.The size of objects is 80 bytes.

# List Comprehension: It executes immediately and return a list.It is enclosed in square brackets.Accessing of element by index is possible.Size of object is 9032 bytes.

## LAMBDA & MAP

# Question 1

celsius = [39.2, 36.5, 37.3, 37.8]
d = list(map(lambda f:(f*9/5)+32, celsius))
print(d)

# Question 2

l = [1,2,3,4,5]
d = list(map(lambda x:x*x,l))
print(d)

## FILTER & REDUCE

# Question 1

l = [1,2,3,4,5,6,7,8,9,10]
for i in range(2,8):
    l = list(filter(lambda x: x == i or x % i,l))
print(l)

# Question 2

from functools import *
l = [1,2,3,4,5]
d = reduce(lambda x,y:x*y,l)
print(d)
