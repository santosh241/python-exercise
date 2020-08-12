# l=[]
# for i in range(2000,3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
#         print(l)

# def fact(x):
#     if(x==0):
#         return 1
#     return x * fact(x-1)
# x=int(input())
# print(fact(x))

# n=int(input())
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
#
# print([d])


# value=input()
# l=value.split(',')
# t=tuple(l)
#
# print(l)
# print(t)


# class InputOutString(object):
#     def __init__(self):
#         self.s = ""
#
#     def getString(self):
#         self.s = input()
#
#     def printString(self):
#        print(self.s.upper())
#
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()


####
# !/usr/bin/env python
# import math
# c=50
# h=30
# value = []
# items=[x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
#
# print(','.join(value))
#
# input_str = raw_input()
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
#
# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col]= row*col
# /
# print multilist
#
# items=[x for x in raw_input().split(',')]
# items.sort()
# print ','.join(items)

# lines = []
# while True:
#     s = raw_input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;
#
# for sentence in lines:
#     print sentence



# s = raw_input()
# words = [word for word in s.split(" ")]
# print " ".join(sorted(list(set(words))))



# value = []
# items=[x for x in raw_input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp%5:
#         value.append(p)
#
# print ','.join(value)



# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print ",".join(values)



# s = raw_input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print "LETTERS", d["LETTERS"]
# print "DIGITS", d["DIGITS"]




# s = raw_input()
# d={"UPPER CASE":0, "LOWER CASE":0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"]+=1
#     elif c.islower():
#         d["LOWER CASE"]+=1
#     else:
#         pass
# print "UPPER CASE", d["UPPER CASE"]
# print "LOWER CASE", d["LOWER CASE"]





