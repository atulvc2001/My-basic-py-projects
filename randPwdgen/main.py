import random

def pwdgen():
    passlen = int(input("what is the password length?\n "))
    s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    pwd = "".join(random.sample(s,passlen))
    print (pwd)

if __name__ == "__main__":
    pwdgen()
