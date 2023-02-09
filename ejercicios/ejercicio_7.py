if __name__ == "__main__":
    print("NÚMERO MÁS GRANDE Y MÁS PEQUEÑO DE UNA LISTA")

    list_numbers = [33, 1, 23, 0, 6, 7, 100, 999, 42 ]
    print(f"La lista dada es: {list_numbers}")

    def num_mayor(list_numbers):
        mayor = list_numbers[0]
        for x in list_numbers:
            if x > mayor:
                mayor = x
        return mayor

    def num_menor(list_numbers):
        menor = list_numbers[0]
        for x in list_numbers:
            if x < menor:
                menor = x
        return menor

    print(f"el número mayor es: {num_mayor(list_numbers)}")

    print(f"el número menor es: {num_menor(list_numbers)}")


    print(f"Utilizando función max de python, el número mayor de la lista es: {max(list_numbers)}")
    print(f"Utilizando función min de python el número menor de la lista es: {min(list_numbers)}")






