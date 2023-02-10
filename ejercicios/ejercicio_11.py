if __name__ == "__main__":
    "NÚMEROS DEL 1 AL 100 EN UNA LISTA"

    def numeros(num):
        list = []
        for i in range(2, num + 1, 2):
            list.append(i)
        return list

    print(numeros(100))











