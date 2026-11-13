def addmultiplenumbers(numbers):

    resultado_suma = 0

    for i in numbers:
        resultado_suma = resultado_suma + i

    return resultado_suma

def multiplymultiplenumbers(numbers):

    resultado = 1

    for i in numbers:
        resultado = resultado * i

    return resultado
def isiteven(num):
    if isinstance(num, int) and num % 2 ==0:
        return True
    else:
        return False
        


def isitaninteger(num):

    return isinstance(num, int)




def main():

    resultado_suma = []

    for i in range(2):
        suma2 = int(input("Ingresa un número: "))
        resultado_suma.append(suma2)

    total = addmultiplenumbers(resultado_suma)

    print("El resultado es:", total)


if __name__ == "__main__":
    main()
