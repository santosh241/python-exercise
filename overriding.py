# Override means having two methods with the same name but doing different tasks.
# It means that one of the methods overrides the other.
#
# If there is any method in the superclass and a method with the same name in a
#  subclass, then by executing the method, the method of the corresponding
#  class will be executed.

class Rectangle():
	def __init__(self,length,breadth):
		self.length = length
		self.breadth = breadth
	def getArea(self):
		print(self.length*self.breadth," is area of rectangle")
class Square(Rectangle):
	def __init__(self,side):
		self.side = side
		Rectangle.__init__(self,side,side)
	def getArea(self):
		print(self.side*self.side," is area of square")
s = Square(4)
r = Rectangle(2,4)
s.getArea()
r.getArea()

