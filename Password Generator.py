import random

def main():

    length = int(input("Enter the length of password: "))
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    print("".join(random.sample(s,length)))


main()