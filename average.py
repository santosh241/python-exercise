n = input("Enter Number to calculate sum")
n = int (n)
average = 0
sum = 0
for num in range(1,n+1,3):
    sum = sum+num
print("SUM of first ", n, "numbers is: ", sum )