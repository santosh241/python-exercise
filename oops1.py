# class-template
# object-instance of the class
# dry-do not repeat your self
# constructor
# Instance and Class Variables
# Decorators
# class methods
# static methods
# inheritance
# polymosphism

# class student:
#     pass
#
#
# sohan=student()
# rohan=student()
#

###the location of both of as differ
# sohan.name="sohan"
# sohan.age=23
# sohan.salary=23000
# sohan.subject=["english","hindi","maths"]
# print(sohan.name)
# print(sohan.age)
# print(sohan.salary,sohan.subject)
#
######################################################333
# class employee:
#     pass
# no_of_leaves=8
#
# sohan=employee()
# rohan=employee()
#
# sohan.name="sohan"
# sohan.salary=25000
# sohan.role="software engineer"
# rohan.name="rohan"
# rohan.salary=26000
# rohan.role="business analyst"
# employee.no_of_leaves=9
# print(employee.no_of_leaves)
# print(sohan.no_of_leaves)
# print(sohan.salary)

###########################



# class Test:
#     ''' class method, static method, class variables, instance variables'''
#     a=10
#     def __init__(self):
#         self.b=20
#         Test.c=30
#     def m1(self):
#         self.d=40
#         Test.e=50
#     @classmethod
#     def m2(cls):
#         cls.f=60
#         Test.g=70
#     @staticmethod
#     def m3():
#         Test.h=80
#
# t=Test()
# t.m1()
# Test.m2()
# Test.m3()
# print(Test.__dict__)
############################################################33
#
#
#
# from datetime import datetime
# class employee:
#     no_of_leaves=8
####constructor (DRY-donot repeat urself.self means jiski baat ho rhi h. init will run always
    # def __init__(self, aname, asalary, arole):
    #     self.name= aname
    #     self.salary= asalary
    #     self.role= arole
    #
    # def know_time():
    #     month = datetime.utcnow()
    #     print("today is ", month)
    #
    #

    # def print_details(self):
    #     return f"my name is {self.name},salary is {self.salary} and role is {self.role}"
#
# rohan = employee("rohan",12000,"python")
# sohan=employee("sohan",45999,"java")
# print(rohan.print_details())
# print(sohan.print_details())
# print(sohan.no_of_leaves)
# employee.know_time()


#####################################################

# class employee:
#     no_of_leaves=8
#     increment = 1.5
#     no_of_employee = 0
#######constructor (DRY-donot repeat urself.self means jiski baat ho rhi h. init will run always
    # def __init__(self, aname, asalary, arole):
    #     self.name= aname  #instance variables
    #     self.salary= asalary
    #     self.role= arole
    #     employee.no_of_employee +=1

    # def increase(self):
    #     pass
        # self.salary = self.salary * employee.increment #self.increment will work but it will go to init first than class

    # def print_details(self):
    #     return f"my name is {self.name},salary is {self.salary} and role is {self.role}"

# print(employee.no_of_employee)
# rohan = employee("rohan",12000,"python")
# sohan=employee("sohan",45999,"java")
# print(rohan.print_details())
# print(sohan.print_details())
# print(sohan.no_of_leaves)
# print(sohan.salary)
# print(sohan.increase())
# print(sohan.salary)
# print(sohan.__dict__)
# print(employee.__dict__)
# print(employee.no_of_employee)
#############################################

# class employee:
#     no_of_leaves = 5
#     increment = 1.5
#     def __init__(self, aname, asalary, arole):
#         self.name= aname
#         self.salary= asalary
#         self.role= arole
#
#     def increase(self):
#         pass
        # self.salary = self.salary * employee.increment #self.increment will work but it will go to init first than class
    #

    # def print_details(self):
    #     return f"my name is {self.name}, and salary is {self.salary} and role is {self.role}"
    #
    # @classmethod
    # def changes_leaves(cls,new_leaves):
    #     cls.no_of_leaves= new_leaves
    #
    # @classmethod
    # def change_increment(cls, amount):
    #     cls.increment = amount
    #
    # @classmethod
    # def from_str(cls, emp_string):
    #     aname, asalary, arole = emp_string.split("-")
    #     return cls(aname, asalary, arole)
    #
    # @staticmethod
    # def isopen(day):
    #     if day=="sunday":
    #         return False
    #     else:
    #         return True
    #
    #
    # @staticmethod
    # def game_player(string):
    #     print("this is good player " + string)


#
# rohan = employee("rohan",12000,"python")
# sohan=employee("sohan",45999,"java")
# raju = employee.from_str("raju-23000-aws")
# print(raju.salary)
# print(rohan.print_details())
# print(rohan.no_of_leaves)
# rohan.changes_leaves(34)
# print(rohan.no_of_leaves)
# print(sohan.salary)
# employee.change_increment(5)
# sohan.increase()
# print(sohan.salary)
# print(sohan.isopen("sunday"))
# employee.game_player("hello")
#
###################################

######inheritance
#
# class Animal:
#     def speak(self):
#         print("Animal Speaking")
######    child class Dog inherits the base class Animal


# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
#
#
# d = Dog()
# print(d.bark())
# print(d.speak())
# print(issubclass(Dog, Animal))

#
# class Animal:
#     def speak(self):
#         print("speaking")
#
#
# class Dog(Animal):
#     def speak(self):
#         print("Barking")
#
#
# d = Dog()
# d.speak()
#
##############
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def printName(self):
#         print(self.name , self.age)
#
# x = Person("john", 99)
# x.printName()
#
# class student(Person):
#     def __init__(self, name, age, year):
#         Person.__init__(self, name, age)
#         self.year = year
#
#     def welcome(self):
#         print("hello " + self.name,+self.age,"year is", + self.year)
#
# x = student("mike", 25, 2009)
# print(x.year)
# x.welcome()
#

###############################################################33

# class employee:
#     no_of_leaves = 5
#     increment = 1.5
#     def __init__(self, aname, asalary, arole):
#         self.name= aname
#         self.salary= asalary
#         self.role= arole
#
#     def increase(self):
#         pass
#         self.salary = self.salary * employee.increment #self.increment will work but it will go to init first than class
#
#
#     def print_details(self):
#         return f"my name is {self.name}, and salary is {self.salary} and role is {self.role}"
#
#     @classmethod
#     def changes_leaves(cls,new_leaves):
#         cls.no_of_leaves= new_leaves
#
#     @classmethod
#     def change_increment(cls, amount):
#         cls.increment = amount
#
#     @classmethod
#     def from_str(cls, emp_string):
#         aname, asalary, arole = emp_string.split("-")
#         return cls(aname, asalary, arole)
#
#     @staticmethod
#     def isopen(day):
#         if day=="sunday":
#             return False
#         else:
#             return True

#
# class Programmer(employee):
#
#     def __init__(self,aname, asalary, arole,lang,exp):
#         super(Programmer, self).__init__(aname, asalary, arole)
#         self.lang=lang
#         self.exp=exp
#
# lohan=Programmer("lohan",30000,'manager',"python",3)
# print(lohan.lang)
# rohan = employee("rohan",12000,"python")
# sohan=employee("sohan",45999,"java")
# raju = employee.from_str("raju-23000-aws")
# print(raju.salary)
# print(rohan.print_details())
# print(rohan.no_of_leaves)
# rohan.changes_leaves(34)
# print(rohan.no_of_leaves)
# print(sohan.salary)
# employee.change_increment(5)
# sohan.increase()
# print(sohan.salary)
# print(sohan.isopen("sunday"))
#
##################################################

# class A:
#     def show(self):
#         print("hello")
#
#
# class B:
#     def test(self):
#         print("test")
#
#
# class C(A,B):
#     def c(self):
#         print("C")
#
#
# class D(C):
#     def demo(self):
#         print("All")
#
#
# d = D()
# d.show()
# d.test()
# d.c()
# d.demo()
#





################################################
###Polymorphism
# '''In Python, polymorphism refers to the way in which different
# object classes can share the same method name, and those methods
# can be called from the same place even though a variety of
# different objects might be passed in.
# '''

# class Dog:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return self.name + ' says Woof!'
#
#
# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return self.name + ' says Meow!'
#
#
# niko = Dog('Niko')
# felix = Cat('Felix')
#
# print(niko.speak())
# print(felix.speak())
#
# '''a few different ways to demonstrate polymorphism'''
# for pet in [niko,felix]:
#     print(pet.speak())
#####
# def pet_speak(pet):
#     print(pet.speak())
#
# pet_speak(niko)
# pet_speak(felix)
#################
# ''' A more common practice is to use abstract classes and inheritance.
#  An abstract class is one that never expects to be instantiated.
#  For example, we will never have an Animal object, only Dog and
#  Cat objects, although Dogs and Cats are derived from Animals'''
#
#
# class Animal:
#     def __init__(self, name):  # Constructor of the class
#         self.name = name
#
#     def speak(self):  # Abstract method, defined by convention only
#         raise NotImplementedError("Subclass must implement abstract method")
#
#
# class Dog(Animal):
#
#     def speak(self):
#         return self.name + ' says Woof!'
#
#
# class Cat(Animal):
#
#     def speak(self):
#         return self.name + ' says Meow!'
#
#
# fido = Dog('Fido')
# isis = Cat('Isis')
#
# print(fido.speak())
# print(isis.speak())
#
##########################3
#
#special methods/Dunder Methods/Magic Methods
#
# class Book:
#     def __init__(self, title, author, pages):
#         print("A book is created")
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)
#
#     def __len__(self):
#         return self.pages
#
#     def __del__(self):
#         print("A book is destroyed")
#
# book = Book("Python Rocks!", "Jose Portilla", 159)
#
# Special Methods
# print(book)
# print(len(book))
# del book