if __name__ == "__main__":
    print("CALCULAR EL FACTORIAL DE UN NÚMERO")

    numero = int(input("Ingrese el número: "))

    def funcion_factorial(numero):

        factorial = 1
        while numero > 0:
            factorial = factorial * numero
            numero -= 1
        return factorial

    funcion_factorial(numero)

    print(f"el factorial del siguiente numero es {funcion_factorial(numero)}")
