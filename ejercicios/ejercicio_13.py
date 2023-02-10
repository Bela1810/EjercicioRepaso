if __name__ == "__main__":
    print("CALCULADORA")

    num_1= float(input("Ingrese el primer número: "))
    num_2 = float(input("Ingrese el segundo número: "))

    while True:
        print("""
        Elegir la operación que desea realizar
        1) Sumar
        2) Restar 
        3) Multiplicar 
        4) Dividir
        """)
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            print("La suma es:", num_1 + num_2)
        elif opcion == 2:
            print("La resta es:", num_1 - num_2)
        elif opcion == 3:
            print("El producto es:", num_1 * num_2)
        elif opcion == 4:
            print("La división es:", num_1 / num_2)
        else:
            print("Opción incorrecta")

