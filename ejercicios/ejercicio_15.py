if __name__ == "__main__":
    print("PALINDROMO")

    # Palíndromo es una palabra que se lee igual al derecho que al revés.

    texto = input("Digite un texto: ")
    aux = 0
    aux2 = 1
    contar = 0

    while (aux < len(texto)):
        if (texto[aux] == texto[len(texto) - aux2]):
            contar += 1
            aux2 += 1
        aux += 1

    if (contar == len(texto)):
        print("Es palíndromo")
    else:
        print("No es palíndromo")