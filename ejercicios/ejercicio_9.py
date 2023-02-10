if __name__ == "__main__":
    print("MATRIZ DE NÚMEROS")

    from random import *

    filas= int(input("Ingrese el número de filas: "))
    columnas= int(input("Ingrese el número de columnas: "))

    num_1 = int(input("Ingrese un primer número: "))
    num_2 = int(input("Ingrese un segundo número mayor al que ingresó anteriormente: "))

    print((f"Los números contenidos en la matriz serán entre {num_1} y {num_2}"))

    matriz = [[randint(num_1, num_2) for i in range(filas)] for j in range(columnas)]

    for f in matriz:
        print(f)

















