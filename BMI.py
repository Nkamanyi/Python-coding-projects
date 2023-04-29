def bmi_calculator(weight, height):
    bmi = weight/(height*height)
    print(f"Your body mass index is: {bmi:.2f}")
    if bmi > 0:
        if bmi <= 16:
            print("You are severely underweight.")
        elif bmi <= 18.5:
            print("You are underweight.")
        elif bmi <= 25:
            print("You are Healthy.")
        elif bmi <= 30:
            print("You are overweight.")
        else:
            print("You are severely overweight.")
    else:
        print("Enter valid detail.s")


def main():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    bmi_calculator(weight,height)

main()