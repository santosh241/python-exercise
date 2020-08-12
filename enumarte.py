#generators

square=(i**2 for i in range(1,100))
print(square)
#
# for num in square:
#     print(num)


list=["mohan","raj","vijay","mohit"]

# pos=0
#
# for name in list:
#     print(f" {pos}----{name}")
#     pos+=1

for pos,list in enumerate(list):
    print(f"{pos}-----{list}")
