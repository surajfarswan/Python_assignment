## CLASSES AND OBJECTS-II

#Question 1

class circle:
    def getArea(self,radius):
        print(3.14*radius*radius)
    def getCircumference(self,radius):
        print(2*3.14*radius)

r = int(input('Enter radius: '))
c = circle()
c.getArea(r)
c.getCircumference(r)

# Question 2

class student:
    def __init__(self,name,rno):
        self.name = name
        self.rno = rno

    def display(self):
        print('\nStudents Details:\n\nName: {}\nRollNo.: {}'.format(self.name,self.rno))

    def setAge(self,age):
        self.age = age
        return self.age

    def setMarks(self,marks):
        self.marks = marks
        return self.marks

n = input('Enter name: ')
r = input('Enter rollno: ')
s1 = student(n,r)
age = int(input('Enter age: '))
marks = int(input('Enter marks: '))
s1.display()
print('Age: ',s1.setAge(age))
print('Marks: ',s1.setMarks(marks))

# Question 3

class temperature:
    def convertFahrenheit(self,cel):
        self.cel = (cel* 9/5)+32
        print('Temperature in Fahrenheit is: ',self.cel)
    def convertCelsius(self,fah):
        self.fah = (fah -32) * 5/9
        print('Temperature in Celsius is: ',self.fah)
n = int(input('Enter value: '))
t1 = temperature()
t1.convertFahrenheit(n)
t1.convertCelsius(n)

# Question 4

class MovieDetails:
    def __init__(self,aname,year,ratings):
        self.aname = aname
        self.year = year
        self.ratings = ratings

    def add(self,name):
        self.name = name
        print('\nMovie Details are:\n\nName of movie: ',self.name)
    def display(self):
        print('Artistname: {}\nYear of release: {}\nRatings: {}'.format(self.aname,self.year,self.ratings))

a = input('Enter artist name: ')
y = input('Enter year: ')
r = input('Enter ratings: ')
m1 = MovieDetails(a,y,r)
name = input('Enter name of movie: ')
m1.add(name)
m1.display()

# Question 5

class Animal:
    def animal_attribute(self):
        return 'Base Class'
    
class Tiger(Animal):
    def tiger_attribute(self):
        pass

a = Animal()
b = Tiger()
print(b.animal_attribute())

# Question 6

#Incorrect code
class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'
class B(A):
    def g(self):
        return 'B'
a = A()
b = B()
print a.f(), b.f()
print a.g(), b.g()

'''In above code there will be error in line 11, line 12 as brackets are missing'''

# correct code will be:

class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'
class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())

'''SO for the corrected code output will be
A B
A B'''

# Question 7

class shape:
    def __init__(self,l,b):
        self.l = l
        self.b = b
        
    def area(self):
        return self.l * self.b

class rectangle(shape):
    def __init__(self,l,b):
        super(rectangle,self).__init__(l,b)

class square(shape):
    def __init__(self,l):
        super(square,self).__init__(l,l)

a = shape(3,6)
b = rectangle(3,6)
c = square(3)
print('Area of rectangle: ',b.area())
print('Area of square: ',c.area())
