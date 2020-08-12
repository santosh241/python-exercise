
l = []
n = int(input("Enter the number of elements in the list"))
for i in range(0,n):
    print(i, end=" ")
    l.append(i)
l.reverse()
print("printing the list items....")
for i in l:
    print(i, end = " ")