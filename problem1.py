name,age,birth = input('Enter name: '),int(input('Enter age: ')),int(input('Enterbirth year: '))
year = birth + 100 - age
print("Hello {},your age is {} and the year you'll turn 100 is {}".format(name,age,year))
