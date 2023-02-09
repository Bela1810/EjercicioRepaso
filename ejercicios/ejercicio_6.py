if __name__ == "__main__":
    print("SUMA DE LOS NÚMEROS DE UNA LISTA DADA")

    list_numbers = [3,7,8,11,6,77,90]
    print(f"la lista configurada es:{list_numbers}")
    suma= 0

    for i in list_numbers:
        suma += i

    print(f"La suma de los números en la lista es {suma}")
