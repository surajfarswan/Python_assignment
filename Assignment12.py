## COMMON MODULES IN PYTHON

# Question 1

'''import datetime as dt
x = dt.date.today()
print(x.strftime("%A"))

# Question 2

import webbrowser
g = input('Enter video name you want to search: ')
webbrowser.open_new_tab('https://www.youtube.com/results?search_query=%s' % g)'''

# Question 3

import os
Dir = os.listdir()
for i in range(1,len(Dir)-1):
    Dir[i],ext = os.path.splitext(Dir[i])
    os.rename(Dir[i]+'.txt',Dir[i]+'(new).jpg')
print(Dir)
