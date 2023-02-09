if __name__ == "__main__":
    print("INVERTIR ORDEN DE LOS ELEMENTOS EN UNA LISTA")

    lista_numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    def invertir_elementos(lista_numeros):
        lista_invertida= []
        contador= len(lista_numeros) - 1
        while contador >= 0:
            lista_invertida.append(lista_numeros[contador])
            contador = contador - 1
        return lista_invertida
    invertir_elementos(lista_numeros)

    print(f"Lista normal dada: {lista_numeros}")
    print(f"lista invertida: {invertir_elementos(lista_numeros)}")

    def funcion_reversed(lista_numeros):
        nueva_lista_invertida= list(reversed(lista_numeros))
        return nueva_lista_invertida
    funcion_reversed(lista_numeros)

    print("------------------------------------------------------------------")
    print(f"Con la función reversed en Python: {funcion_reversed(lista_numeros)}")



