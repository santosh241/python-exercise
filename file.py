#file basics
#
# r        Opens a file for reading only.
# rb   Opens a file for reading only in binary format.
# r+   Opens a file for both reading and writing.
# rb+  Opens a file for both reading and writing in binary format.
# w        Opens a file for writing only.
# wb   Opens a file for writing only in binary format.
# w+   Opens a file for both writing and reading.
# wb+  Opens a file for both writing and reading in binary format.
# a        Opens a file for appending.
# ab   Opens a file for appending in binary format.
# a+   Opens a file for both appending and reading.
# ab+  Opens a file for both appending and reading in binary format.

# f = open("mhn.txt", 'r')
# info = f.read()
# print(info)
# f = open("mhn.txt", 'w')
# f.write("hey whats up :)")#it takes only string values
#
# f=open("mhn.txt","w") #this will over ride previous text.
# f.write("sohan bahut achha hai")
#
# f=open("mhn.txt", "a") #this will append
# f.write("he is a good boy")

# print(f.tell()) #this will tell you the index location
#
# f.seek(0) #it will send your curson to the specified index
# f=open("mhn.txt", "w") #this will append
# f.write("he is a bad gd boy")

#
# f = open("mhn.txt", "r+")
# f.write("sohan is a  bad boy")

# f=open("mhn.txt","a")
# f.write("mohan is a good boy")
# print(f)
# f=open("mhn.txt","r+")
# v = f.read()
# print(v)
# for file in f:
#   print(file)
# f.close()

# f=open("mhn.txt","r+")
# content=f.read()
# f.seek(0)
# print(content)
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.seek(0)
# print(f.readlines())
# f.seek(0)
# f=open("mhn.txt","r+")
# f.seek(0)
# content=f.read()
# print(content)
# for file in f:
#     print(file, end="")
#
# f.close()

# l = [1,2,3,4,5,6]
# for i in l:
#     print(i,end="")
# contents=f.readlines()
# print(contents)
# f.close()
# f.closed()# closed is attribute
# f.seek(0)
# contents.insert(3, "hello this is ")
# f.seek(0)
# print(contents)
# print(f.readlines())
# f=open("math.txt", "w+")
# contents= "".join(contents)
# f.write(contents)
# f.seek(0)
# print(f.readlines())

# f.close()


# def text_demo():
#     d = open('sohan.txt', 'r+')
#     d.write("hi you are great....")
#     print(d.read(2))
#     print(d.readable())
#     print(d.writable())
#     print(d.closed) # false
#     d.close()
#     print(d.closed) # true


# text_demo()

#
# def operation():
#     f = open('sohan.txt')
#     print(f.read(5))
#     print(f.tell())
#     print(f.read(5))
#     print(f.tell())
#     f.seek(15)
#     print(f.tell())
#     print(f.read())
#
# operation()

##########################################################

def sign_up():
    name = input("enter your name: \n")
    passwword = input("enter your password: \n")
    email = input("enter your email: \n")
    with open('signup.txt','w') as f:
        f.write(name+'\n')
        f.write(passwword+'\n')
        f.write(email+'\n')
    print("write date successfully!!!")


def login():
    email = input("enter your email: \n")
    passwword = input("enter your password: \n")
    with open('signup.txt') as f:
        info = f.readlines()
        pwd = info[1].strip()
        email_m = info[2].strip()
        if email == email_m and passwword == pwd:
            print("success")
        else:
            print("Login Failed")
sign_up()
login()


def csv_operation():
    import csv
    f = open('stu.csv','w',newline='')
    wr = csv.writer(f)
    wr.writerow(['Name','Roll','Age','Marks'])
    wr.writerow(['A',123,23,79])
    wr.writerow(['A',123,23,79])
    wr.writerow(['A',123,23,79])
    wr.writerow(['A',123,23,79])
    wr.writerow(['A',123,23,79])
    wr.writerow(['A',123,23,79])
    wr.writerow(['A',123,23,79])
    f.close()

csv_operation()
#
def csv_demo():
    import csv
    with open('emp.csv', 'w', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(['Employee Name', 'Employee Department', 'Employee Salary'])
        while True:
            name = input("enter your name: ")
            dept = input("enter your dept: ")
            sal = input("enter your sal: ")
            wr.writerow([name, dept, sal])
            ch = input("enter your choice!!")
            if ch[0].lower() == 'n':
                break
            else:
                continue
csv_demo()

def read_csv():
    import csv
    with open('emp.csv') as f:
        r = csv.reader(f)
        for i in r:
            for j in i:
                print(j)
#
read_csv()
#
def list_dump_csv():
    import csv
    name = ['A', 'B', 'C', 'D', 'E']
    sal = [1234, 3456, 232435, 2345, 21345]
    em_id = [101, 102, 103, 104, 105]
    dept = ['IT', 'Sales', 'HR', 'Engineering', 'MECH']
    addreess = ['Noida', ' delhi', 'GUrgiadn', 'qwer', 'asdfg']
    with open('listcsv.csv', 'w', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(['Name', 'Salary', 'EmpId', 'Dept', 'Address'])
        for i, j, k, l, m in zip(name, sal, em_id, dept, addreess):
            wr.writerow([i, j, k, l, m])
        print("Write data successfully")

#
if __name__ == '__main__':
    list_dump_csv()