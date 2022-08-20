Numero, divisor = int(input("Digita el numero: ")), int(
    input("digita otro numero: "))


def Maximo_comun_divisor(a, b):
    temporal = 0

    while b != 0:
        temporal = b
        b = a % b
        a = temporal
        print(a)
    return a


print("_____________________________________")
print(Maximo_comun_divisor(Numero, divisor))
