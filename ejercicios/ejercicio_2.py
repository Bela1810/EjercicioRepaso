if __name__ == "__main__":

    import math
    radio = int(input("Ingrese el radio del circulo: "))
    pi = math.pi

    def area_circulo():
        area = pi * (radio * radio)
        return area

    area_circulo()

    print(f"el area del circulo es: {area_circulo()}")
