
def guess_check(guess, answer):
    attempts = 0
    score = 0

    while True and attempts < 3:
        if guess == answer:
            print("Correct answer")
            score +=1
            attempts +=1
            break
        else:
            if attempts < 2:
                guess = input("Sorry wrong answer, try again ")
            attempts += 1
        if attempts == 3:
            print(f"The correct answer is {answer}.")
    print(f"Number of attempts: {attempts}")
    print(f"Your score is: {score}")

def main():
    print("Please guess the animal :)")
    guess = input("Which bear lives at the North pole? ")
    guess_check(guess, "polar bear")

main()