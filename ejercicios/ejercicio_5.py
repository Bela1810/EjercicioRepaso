if __name__ == "__main__":
    print("CELSIUS TO FAHRENHEIT")

    celsius_value = int(input("Enter number on Celsius: "))

    def fuction_fahrenheit():
        calculation_fahrenheit = (celsius_value * (9/5)) + 32
        return calculation_fahrenheit

    fuction_fahrenheit()

    print(f"To Fahrenheit is {fuction_fahrenheit()}")