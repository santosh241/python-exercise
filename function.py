def main():
    print("hello world!")


main()
print("print mee")
#
#
# #built_in_function
# a=9
# b=8
# c=sum((a,b))
# print(c)
# #user_define_function

# a=9
# b=8
# c=a+b
# print(c)

def function(a,b):
    print("your are in function one" , a+b)

function(6,7)
#
def function1(a,b):
    """ this method use for add two number"""
    average=(a+b)/2
    return average
v=function1(6,8)
print(v)
print(function1.__doc__)
#
#
def wish():
    return "hello good morning"
print(wish())
#
#
def sum(a,b):
    print("sum of two number",a+b)
sum(5,10)


a=int(input("enter your first value"))
b=int(input("enter your second value"))
def sum(c,d):
   print("sum of two numbers",a+b)
sum(a,b)
#
def sum(c,a=10,b=20):
    print("sum of two number",a+b+c)
sum(a=20,c=10)
#

class Circle:
    pi = 3.14

    ##########Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    ####Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

###    Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


c = Circle()

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())