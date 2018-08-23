## DICTIONARIES

# Question 1

d = {}
n = int(input('Enter: '))
for i in range(0,n):
    j = input()
    d[j] = input()
print(d)

# Question 2

d1 = {}
d2 = {}
n1 = int(input('Enter no. of names: '))
for i in range(0,n1):
    d2 = {}
    name = input('Enter name: ')
    n2 = int(input('Enter no. of subjects: '))
    for j in range(0,n2):
        sub = input('Enter subject: ')
        marks = int(input('Enter marks: '))
        d2[sub] = marks
    d1[name] = d2
print(d1)
stu = input('Enter student name: ')
print(d1[stu])
