if __name__ == "__main__":
    print("PROGRAM TO CALCULATE THE AREA OF A CIRCLE")
    import math

    radio = int(input("Enter the radio: "))
    pi = math.pi

    def circle_area():
        area = pi * (radio * radio)
        return area

    circle_area()

    print(f"el area del circulo es: {circle_area()}")
