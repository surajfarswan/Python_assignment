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

import random
with open('r1.txt','w+') as f:
    for i in range(10):
        f.write(str(random.randint(0,9)))
        f.write('\n')
with open('r1.txt') as f1,open('r2.txt','w+') as f2:
    l = []
    for line in f1:
        l.append(int(line.strip('\n')))
    l = sorted(l)
    for i in l:
        f2.write(str(i)+'\n')
with open('r2.txt') as f:
    for i in f:
        print(i.strip('\n'))
