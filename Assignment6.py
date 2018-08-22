## FUNCTIONS

#Question 1

def area(num):
    a = 4*3.14*num*num
    print('Area of sphere is: ',a)
    
r = float(input('Enter radius: '))
area(r)

# Question 2

def perfect(n):
    s = 0
    for j in range(1,n):
        if n%j == 0:
            s += j
    if s == n:
        print('Perfect number: ',n)
for i in range(1,1001):
    perfect(i)

# Question 3

def table(n):
    for i in range(1,11):
        print(n,' * ',i,' = ',n*i)

n = int(input('Enter number: '))
table(n)

# Question 4

def power(base,exp):
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return base*power(base,exp-1)

b = int(input('Enter base value: '))
e = int(input('Enter power value: '))
print('Output: ',power(b,e))
