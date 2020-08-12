def smart(func):
    def inner(a,b):
        if b==0:
           print("cannot divide by zero")
        else:
             func(a,b)
    return inner
@smart
def calc(a,b):
    print("division is",a/b )

calc(10,20)
calc(20,27)
calc(10,0)

