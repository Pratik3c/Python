"""variables"""

# sher = "harsh bhaiya"

# SheryiansSchool = "students" #pascal case

# sheryiansSchool = "students" #camel case

# sheryians_school = "students" #snake case




"""data types"""

# a = -34

# b = 56.8
# c = 12/3

# v = 34j

# print(type(v))



# st = '1231243235 dsagaiogiaeb !@#$%^&*'

# print(type(st))

# b = True

# t = False

# print(type(b))


"""strings"""

# a = "SHER CODER"


# print(a[::])

# a = 12 

# print(12/3)

# name = "akarsh"
# age = "23"
# print(f"my name is {name} and my age is {age}")

# age = int(input("hello what is your age"))
# print(age)


# p = int(input("Enter first number: "))
# q = int(input("Enter second number: "))

# print(f"Sum of number is {p+q}")



""" operators """
# a = 5
# b = 32


# print(a + b)
# print(b - a)
# print(a * b)
# print(b/a)    # this will return the answer in float since any "p/q" form is "float".
# print(b//a)   # this is floor division --> gives number before decimal.
# print(5**100)
# print(32%5)


# print(12+4/2)  # BODMAS is followed


#assignment operators 
# a = 23

#compound assignmet operations

# a = 20

# a += 20
# a += 40
# a += 60
# a-=
# a*=
# a/=
# a//=
# a**=

# print(a)

# a = 12.1
# b = 12 

# print(a == b)

# print(a != b)

# print(a > b)
# print(45 < 67)
# print(23 >= 23)
# print(45 <= 45)


# print(ord("A"))
# print(ord("B"))

# print("ABC" > "ACD")

# print("A" > 34)

# print(12 >20 and 123 > 100 and 34 == 34 and 45 < 90)

# print(12 !=12 or 23 ==45 or 67 == 56 or 10 > 5)

# print(not 12 == 12)



""" Conditional Statement """
#IF else 

# a = 6

# if a > 10:
#     print("I will do task A")

# else:
#     print("I will do task B")

# money = int(input("please provide me the money :- "))

# if money == 10:
#     print("I will have a choco bar icecream")

# elif money == 20:
#     print("I will have a mangodolly")

# elif money == 30:
#     print("I will have a frosty")
    
# else:
#     print("I will have a cone")

# num1 = int(input("pleae tell your first number "))
# num2 = int(input("pleae tell your second number "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")
# else:
#     print("Both the numbers are same")


# gen = input("please tell your gender as character (M or F):-")

# if gen == 'M' or gen == 'm':
#     print("Good morning SIR")
# elif gen == "F" or gen == 'f':
#     print("Good morning MAM")
# else:
#     print("Unidentified gender")


# num = int(input("please tell your number :- "))

# if num%2 == 0:
#     print("even number")

# else:
#     print("Odd number")

# name = input("please tell your name : - ")
# age = int(input("now tell your age :- "))

# if age >=18 :
#     print(f"hello {name} you are a valid vote")

# else:
#     print(f"hello {name} you are not a valid vote")

# year = int(input("tell your year :- "))

# if year %100 == 0 and year %400 == 0:
#     print("Its a leap year")

# elif  year %100 != 0 and year %4 ==0:
#     print("Its a leap year")

# else:
#     print("its a normal year")

# t = int(input("please tell the temprature :- "))

# if t < 0:
#     print("Freezing cold")

# elif t >= 0 and t <10:
#     print("very cold")

# elif t >= 10 and t <20:
#     print("cold")

# elif t >= 20 and t <30:
#     print("plesant")

# elif t >= 30 and t <40:
#     print("hot")

# else:
#     print("temprature is very hot ")


# print("hello world ")



#For loop
# range(start,stop,step) ; default value of start=0,step=1.

# a=range(1,20,3)
# for i in a:
#   print(i)


#lets print a table of 5
# n = int(input("Which table you want ? "))

# for i in range(n,(n*10)+1,n):
#     print(i)


# a = "SHERYIANS TEACHES INDUSTRY THINGS"
# print(len(a))

# for i in range(len(a)):
#     print(a[i])

# other way
# a = "SHERYIANS IS COOL"

# for i in a:
#     print(i)


### for with else --> if break✅,else❌ ; if break❌,else✅

# for i in range(1,21):
#     if i == 56:
#         print("break statement is executed")
#         break
#     print(i)

# else:
#     print("Break statement is not executed")


# n = int(input("please tell your number"))

# for i in range(n):
#     print("hello world ")

# n = int(input("please tell your number "))

# for i in range(1,n+1):
#     print(i)

# n = int(input("please tell your number "))

# for i in range(n,0,-1):
#     print(i)


# n = int(input("which table you want : - "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")


# n = int(input("please tell your number:- "))

# sum = 0 

# for i in range(1,n+1):
#     sum = sum + i


# print(f"your sum is {sum}")

# n = int(input("please tell your number:- "))

# fact = 1 

# for i in range(1,n+1):
#     fact = fact * i


# print(f"your factorial is {fact}")


# n = int(input("tell your number :- "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i

# print(f"your even and odd sum are {even} , {odd}")


# n =int(input("which number factors you want :- "))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)


# n = int(input("check your number is perfect or not :-"))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i

# if sum == n:
#     print("your number is perfect")
# else:
#     print("not a perfect number")




# n = int(input("check your number is prime or not  :-"))

# count = 0

# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1

# if count == 2:
#     print("your number is prime")
# else:
#     print("your number is not prime")


# a = "SHERYIANS"

# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# print(b)

# a = "NAMAN"

# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]


# if b == a:
#     print("your string is pallindrome")

# else:
#     print("its not a pallindrome")

# a = "sdfsogn12413@#$%^&U"

# char = 0
# dig = 0
# spchr = 0

# for i in a:
#     if i.isdigit():
#         dig +=1 
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr +=1 

# print(f"your digits are {dig}\nyour alphabets are {char}\nyour special characters are {spchr}")

# print(dir(str))



# a = 1 
# while a <= 30:
#     print(a)
#     a = a + 1


# a = int(input("tell your number"))

# rev = 0

# while a > 0:
#     rev = rev *10 + a % 10
#     a = a //10

# print(rev)


# a = int(input("tell your number"))

# copy = a
# rev = 0

# while a > 0:
#     rev = rev *10 + a % 10
#     a = a //10

# if copy == rev:
#     print("pallindromic number")
# else:
#     print("not a pallindromic number")



# import random

# num = random.randint(1,10)

# tries = 0

# while True:
#     guess = int(input("please guess your number between 1 and 10 :- "))
#     if num == guess:
#         tries +=1
#         print(f"you are right you guessed the number is {tries} tries")
#         break

#     elif num < guess:
#         print("go a little lower")
#         tries +=1
    
#     elif num > guess:
#         print("go a little higher")
#         tries +=1

#     else:
#         tries +=1 
#         print("sorry you are wrong")



"""function"""
# print(12)


# def hello():
#     print("this is a hello function so I am doing hello")


# hello()


# def hello(name,age):
#     print(f"your name is {name} and your age is {age}")

# hello(age = 22,name = "akarsh")


# def pallindrome(st):
#     rev = ""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]
    
#     if rev == st:
#         print(f"{st} is a pallindrome")
#     else:
#         print(f"{st} is not a not a pallindrome")


# pallindrome("NAMAN")
# pallindrome("CURSOR")


# def hello():
#     return "hello how are you"

# print(hello())


# def sum(a,b):
#   return f"The sum of {a} and {b} is {a+b}"

# print(sum(4,5))


"""in-built data structures --> list,tuple,dictionary,set"""

# List
a = [12,13,14,15,16,34.5,True,print(),"Hello"]

# we can do indexing and slicing in list as we did for string
# print(a[2])
# print(a[0:5])

# String are immutable, List are mutable...
# str = "Pratik"
# str[0] = 'Q'
# print(str)


# #1st way using index

# for i in range(len(a)):
#     print(a[i])

# #2nd way directly on values

# for i in a:
#     print(i)

# l = [-45,67,12,-68,-69,34]

# print("positive elements are ")
# for i in l:
#     if i >= 0:
#         print(i)

# print("negative elements are")
# for i in l:
#     if i < 0:
#         print(i)

# l = [12,435,67,89,23,25,69]

# sum = 0

# for i in l:
#     sum = sum + i

# print(sum/len(l))



# l = [12,567,43,235,347,568,45,7]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f"your largest number is {largest} at index {index}")


# l = [12,16,13,19,17]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i


# print(sec_largest, largest)



# a = [12,13,18,15,16]

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")


# tuple
# a = (1,2,3,4,5,5,5.5,print(),"hello")

# count = a.count(5)
# print(count)

# concept of tuple unpacking
# a,b,c,d = (1,2,3,4)
# print(b)


# a = (1)
# print(type(a))  # o/p : int

# a = (1,)
# print(type(a))  # o/p : tuple


# Set
# a = {1,8,9,"hello",2,3,4,5}

# for i in a:
#     print(i)    # prints in random order each time


# a = {8,1,2,3,4}
# a.remove(2)
# poped_element = a.pop()   # remove random value
# a.clear()

# print(a)


# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# b -= a

# print(b)



# dictionary
# d = {10:100,20:200,30:300,40:400}

# d[10] = 700 # updating
# d[50] = 500 # creating
# del d[30]   # deleting 

# print(d)


""" Deep and Shallow copy"""
# import copy

# # Original list with nested list
# original = [1, 2, [3, 4]]

# # Shallow copy
# shallow = copy.copy(original)

# # Modify nested object
# shallow[2][0] = 99

# print("Original:", original)   # [1, 2, [99, 4]]
# print("Shallow:", shallow)     # [1, 2, [99, 4]]

##############################################################
# import copy

# # Original list with nested list
# original = [1, 2, [3, 4]]

# # Deep copy
# deep = copy.deepcopy(original)

# # Modify nested object
# deep[2][0] = 99

# print("Original:", original)  # [1, 2, [3, 4]]
# print("Deep:", deep)          # [1, 2, [99, 4]]





# d = {10:100,20:200,30:300,40:400}

# print(d.items())

# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}

# merge two dict
# for i in d2:
#     d1[i] = d2[i]

# print(d1)


# d1 = {10:100,20:200,40:300}
# sum = 0

# for i in d1:
#     sum = sum + d1[i]

# print(sum)


# a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]

# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] +=1 
#     else:
#         d[i] = 1

# print(d)


# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]



""" Exception Handling """
# a = int(input("tell your number :- "))

# try:
#     print(10/a)

# except Exception as err:
#     print(f"sorry there is an err as {err}")

# else:
#     print("good there is no exception")

# finally:
#     print("i will run no matter what")


# print("ok i have done the division")   # to show normal flow

### except and else are connected if one works other does not...


# raise custom error
# age = int(input("tell your age :- "))

# try:

#     if age < 10 or age > 18:
#         raise ValueError("your age must be between 10 and 18")
#     else:
#         print("welcome to the club")

# except Exception as err:
#     print(f"an error occured as {err}")


# print("the club will start soon")




#File handling

# r = open("superman.txt",'a')

# r.write("and now I am appending some content inside the file  ")

# r.close()




# class Factory:
#     a = 12 # attribute 

#     def hello(self): #method, self --> points to the currect instance of class(caller object).
#         print("how are you")
    
#     print("Hello i am getting initalized!")   # this will run only once, first time when the class gets initalized.

# print(Factory().a)
# Factory().hello()


# obj = Factory()
# print(obj.a)

# obj2 = Factory()


# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
    
#     def show(self):
#         print(f"your object details are {self.material}, {self.pockets},{self.zips} ")
    


# reebok = Factory("leather",3,2)   #self points to the location of reebok object.

# campus = Factory("nylon",3,3)

# reebok.show()

   

# class Animal:
#     name = "lion"      #class attribute
    
#     def __init__(self,age):
#         self.age = age #instance attribute
    
#     def show(self):  #instance method --> targets the instance, and requires 1 parameter as self otherwise we get error
#         print(f"how are you ,your age is {self.age}")
    
#     @classmethod        # class method --> targets the class
#     def hello(cls):
#         print(f"how are you brother {cls.age}")  # class methods can't access the instance attribute

#     @staticmethod
#     def static():
#         print("how are you")

   

# obj = Animal(12)

# obj.show()
# obj.hello()
# obj.static()

"""Inheritance"""

# class Factorymumbai: #parent class / superclass
#     a = "I am an attribute mentioned inside Factory"
#     def hello(self):
#         print("hello I am a method mentioned inside Factory")

# class Factorypune(Factorymumbai):   #child class /subclass
#     pass

# obj = Factorymumbai()

# obj2 = Factorypune()

# obj2.hello()


# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def show(self):
#         print(f"hello your name is {self.name}")
    
# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age
    
#     def show(self):
#         print(f"hello your name is {self.name},{self.age}")


# animal1 = Animal("lion")
# person1 = Human("akarsh",23)

# animal1.show()


# class Animal:
#     def __init__(self,name):
#         pass

# class Human:
#     def __init__(self,name,age):
#         pass

# class Robots(Human,Animal):    #order matters
#     name3 = "charli123"

# obj = Robots()           #it will ask for both name and age




# class Factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips 
    
# class BhopalFactory(Factory):
#     def __init__(self, material, zips,color):
#         super().__init__(material, zips)
#         self.color = color
    
# class Punefactory(BhopalFactory):
#     def __init__(self, material, zips, color,pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets


""" Polymorphism """
#Method Overriding
# class Animal:
#     def show(self):
#         print("hello I am akarsh")

# class Human(Animal):
#     def show(self):
#         print("how are you")

# obj = Human()
# obj.show()         # show() of Human gets executed, this is method overriding

### There is no method overloading like in other languages, the function will get over writted by the latest function.

#Duck Typing
# class Animal:
#     def show(self):
#         print("I am showing ")

# class Human:
#     def show(self):
#         print("hello I am also showing ")

# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show()



"""Encapsulation"""
# class Factory:
#     __a = "pune"

#     def show(self):
#         print(Factory.__a)


# obj = Factory()

# obj.show()


""" Abstraction """
# from abc import ABC, abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass 
    
#     @abstractmethod
#     def area(self):
#         pass

# class Square(abstract):
#     def __init__(self,side):
#         self.side = side

#     def perimeter(self):
#         print("i have created")
    
#     def area(self):
#         print("I have created this ")



# class Circle(abstract):
#     def __init__(self,radius):
#         self.radius = radius
    
#     def perimeter(self):
#         print("i have created")
    
#     def area(self):
#         print("I have created this ")

# obj = Circle(7)
# obj2 = Square(12)


"""Dunder Methods"""
# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"hello how are you and your name is {self.name}"

#     def __add__(self,other):
#         sum = 0
#         for i in other:
#             sum = sum + i.age

#         return f"your sum of ages are {self.age + sum}"

# obj = Animal("lion",12)
# obj2 = Animal("dolphin",14)
# obj3 = Animal("tiger",34)

# print(obj + (obj2,obj3))



""" Advance Stuff """
# class Animal:
#     @property
#     def show(self):
#         print("hello how are you")
    
# obj = Animal()

# obj.show       # @property helps to call method without '()'



# def decorate(func):                                    # decorater captures the function
#     def wrapper(a,b):                                  # wrapper captures the arguments
#         print("the addition to your numbers are ")
#         func(a,b)
#         print("thankyou I hope you liked it ")
#     return wrapper

# @decorate
# def addition(a,b):
#     print(f"your total is {a + b} ")

# addition(12,67)


""" Args """
# def addition(*args):        # after "*" what we write becomes tuple
#   sum=0
#   for i in args:
#     sum = sum + i

#   print(sum)

# addition(12,12,34,24)

""" Kwargs --> KeyWord Arguments """
# def show(**kwargs):        # after "**" what we write becomes dictionary(key:value)
#   print(kwargs)

# show(b=12,a=12,c=34,d=24)  # o/p : {'b': 12, 'a': 12, 'c': 34, 'd': 24} 


# def information(**kwargs):
#     print("your information is\n\n ")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")
    
# information(name = "Akarsh", age = 23, designation = "AI/ML")



# def decorate(func):                                    # decorater captures the function
#     def wrapper(*args,**kwargs):                       # wrapper captures the arguments
#         print("the addition to your numbers are ")
#         func(*args,**kwargs)
#         print("thankyou I hope you liked it ")
#     return wrapper

# @decorate
# def addition(a,b):
#     print(f"your total is {a + b} ")

# addition(12,67)


""" Ternary Oprator """
# value_if_true if condition else value_if_false

#example
# x=15
# result = "Even" if x%2==0 else "Odd"
# print(result)

## I want to store and print all the even numbers from 1 to 20
# l = []
# for i in range(1,21):
#   if i%2==0:
#     l.append(i)

# print(l)

## Let's do it in one line using "list/set/dictionary comphrehension" --> "what_we_want_to_append loop conditon"
# l = [i for i in range(1,21) if i%2==0]
# print(l)


# l = {i : i**2 for i in range(1,10)}
# print(l)


""" lambda function """
# addition = lambda a,b : a+b     # lambda _key_word arguments : expression
# print(addition(12,13))





# a = [1,2,3,4,5]

# def double(x):
#     return x *2

# result = map(double,a)
# print(list(result))


""" modules --> single .py file"""
# print(calc.addition(12,23))     # let's say we have calc.py with addition function defined in it.

""" packages --> collection of .py file"""
# from modelss import hello,maths



""" Pattern printing """
# a = int(input("how many rows you  want "))

# for i in range(1,a + 1):
#     for j in range(i):
#         print("* ",end = "")
#     print()


# n = int(input("tell how many rows you want"))

# for i in range(1,n+1):
#     for j in range(n-i):
#         print("  ",end = "")
#     for k in range(i):
#         print("* ",end = "")
#     print()



# n = int(input("tell how many rows you want"))

# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end = "")
#     for k in range(i):
#         print("* ",end = "")
#     print()


# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end = "")
#     for k in range(i):
#         print("* ",end = "")
#     print()

# a = 1234
# copy = a
# sum = 0

# while a > 0:
#     z = a %10
#     fact = 1 
#     for i in range(1,z+1):
#         fact = fact * i
    
#     sum = sum + fact
#     a = a//10 

# if sum == copy:
#     print("this is a strong number ")
# else:
#     print("not a strong number")


# for j in range(2,21):
#     a = j

#     for i in range(2,(a//2)+1):
#         if a % i == 0:
#             break

#     else:
#         print(a)



# a = [1,1,1,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,5,5,5]
# count = 0
# dict = {}
# for i in a:
#     if i in dict.keys():
#         dict[i] +=1 
#     else:
#         dict[i] = 1
# max = 0
# for i in dict.values():
#     if i > max:
#         max = i
# for i in dict:
#     if dict[i] == max:
#         print(f"{i} occured {max} times and that is largest occurence")
#         break