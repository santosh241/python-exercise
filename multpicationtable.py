# Python Program to Print Multiplication Table of a Number

num = int(input("Enter the number: "))

print("Multiplication Table of", num)
for i in range(1, 11):
   print(num,"X",i,"=",num * i)