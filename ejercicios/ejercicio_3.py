if __name__ == "__main__":

    import random
    numeros_generados = int(input("Ingrese cuantos numeros desea generar: "))
    num_1= int(input("Ingrese el primer número: "))
    num_2= int(input("Ingrese el segundo número: "))

    print(f"se van a generar números entre {num_1} y {num_2}")

    for x in range(numeros_generados):
        print(random.randint(num_1,num_2))