name = ["mohan", "raj", "harsh"]
# print(name)
# number=[23,45,29,59,34]
# print(number)
# mixed=["mohan","raj","harsh",23,45,29,59,34]
# print(mixed)
# mixed_int=[23,45,29,59,34]
# mixed_int.sort()
# print(mixed_int)
# name.append("sohan")
# print(name)
# name.insert(2,"ravi")
# print(name)
# name.extend([2,3,4,5,6,7,8])
# print(name)
# name.pop()
# print(name)
# name.remove("ravi")
# print(name)
# name.clear()
# print(name)
# name.sort()
# print(name)
# copy_name=name.copy()
# print(name)
# print(copy_name)
# copy_name[0]='sohan'
# print(copy_name)
# print(name)
# # # name.sort()
# # # print(name)
# # # print(copy_name)
# # #############################
# # ######################
# mylist=[1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4]
# mylist=set([1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4])
# print(mylist)
# # #######################
l = [3, 7, [1, 4, 'hello']]
l[2][2] = 'goodbye'
print(l)
# tupledict=dict(name="raju",age=23,role="baaa")
# print(tupledict)
# s={1,2,2,3,43,4,45,5,5,1,2,3}
# print(s)
# # ###############################33
number = [1, 2, 3, 4, 5]
square = [i ** 2 for i in number]
print(square)
# #
number = [1, 2, 3, 4, 5]
squre = [x ** 2 for x in number if x % 2 == 1]
print(squre)
# #
# # number_list = [ x**2 for x in range(20) if x % 2 == 0]
# # print(number_list)
# #
my_list = [('a', 232),
           ('b', 343),
           ('c', 543),
           ('d', 23)]
# # #output should be  [('a', 'b', 'c', 'd'), (232, 343, 543, 23)]
# #
c = list(zip(*my_list))
print(c)
# #
# #
# mixed=["mohan","23","raj","34"]
# mixed.sort()
# print(mixed)
# #
#
# del name[3]
# print(name)
# #
# # #name.sort()
# # #print(name)
# # number.sort()
# # print(number)
# # mixed.sort()
# # print(mixed)
# # print(sorted(name))
# # print(name)
# #
# # name.reverse()
# # print(name)
# #
# # cpoy_1=name.copy()
# # print(cpoy_1)
# # name[1]="madhuri"
# # print(name)


tuple

# tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida')
# tup2 = (1,2,3,4,5,6,7)
# print(tup1[0])
# print(tup2[1:4])

# #Packing and Unpacking
# x = ("webtrackker", 20, "Education")    # tuple packing
# (company, emp, profile) = x    # tuple unpacking
# print (company)
# print (emp)
# print (profile)
# print(x)

# #Comparing tuples
# case 1
a = (5, 6)
b = (1, 4)
if (a > b):
    print("a is bigger")
else:
    print("b is bigger")
#
# #case 2
a = (5, 6)
b = (5, 4)
if (a > b):
    print("a is bigger")
else:
    print("b is bigger")

# #case 3
a = (5, 6)
b = (6, 4)
if (a > b):
    print("a is bigger")
else:
    print("b is bigger")

# #Tuples and dictionary
dict = {'x': 100, 'y': 200}
b = dict.items()
print(b)

# #Slicing of Tuple
x = ("a", "b", "c", "d", "e")
print(x[2:4])