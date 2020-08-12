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
