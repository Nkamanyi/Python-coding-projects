import random

def main():
    min_val = 1
    max_val = 6

    while True:
        print("Rolling the dice...")
        print("The values are:")

        for i in range(1,3):
            print(random.randint(min_val,max_val))
        que = (input("Do you want to play again? (Yes/No): ")).lower()
        if que == "no":
            print("Thanks for coming around :)")
            break


main()