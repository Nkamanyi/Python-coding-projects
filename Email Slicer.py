def main():

    email = input("Enter your email address: ")
    word = email.split("@")
    print(f"Your username is '{word[0]}' and your domain is '{word[1]}'")

main()