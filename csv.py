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