if __name__ == "__main__":
    print("MEDIA ARITMETICA")

    def media(lista):
        acum = 0
        for i in range(len(lista)):
            acum += lista[i]
        return acum / len(lista)


    lista = [5, 2, 3, 7, 1, 8]
    print("La media aritmética de la lista es ", media(lista))