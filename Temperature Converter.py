def temperature_converter(temperature):

    celsius = print(f"{((temperature - 32) * 5/9):.2f}")
    return celsius


def main():
    temperature = float(input("Enter temperature: "))
    temperature_converter(temperature)


main()