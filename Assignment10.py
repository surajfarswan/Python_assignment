## FILE HANDLING

# Question 1

f = open('abc.txt','r')
l = f.readlines()
for i in l:
    print(i)
f.close()

# Question 2

from collections import Counter
with open('abc.txt','r') as f:
    a = Counter(f.read().split())
    print(a)

# Question 3

with open('abc.txt','r') as f:
    with open('new.txt','w') as g:
        for l in f:
            g.write(l)

# Question 4

with open('abc.txt') as f:
    with open('new.txt') as g:
        for l1,l2 in zip(f,g):
            print(l1+l2)

# Question 5

f = open('a.txt')
c = []
for l in f:
    c.append(int(l))
c.sort()
print(c)
f.close()
