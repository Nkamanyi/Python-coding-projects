

def main():
    Acronym = ""

    phrase = input("Enter a phrase: ")
    for word in phrase.split():
        Acronym += word[0].capitalize()

    print(Acronym)

main()
