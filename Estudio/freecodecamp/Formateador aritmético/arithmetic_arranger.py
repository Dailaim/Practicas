def comparador(listA, listB):
    salida = []
    for i in range(len(listA)):
        Entrada = []
        Entrada.append(len(listA[i]))
        Entrada.append(len(listB[i]))
        salida.append(max(Entrada))
    return salida


def lendigitos(valorA, valorB):

    if len(valorA) < 6 and len(valorB) < 6:
        return [None, False]
    else:
        return ["Error: Numbers cannot be more than four digits.", True]


def digitos(valorA, valorB):
    validar = [None, None]
    validar[0] = valorA.isdigit()
    validar[1] = valorB.isdigit()
    if False in validar:
        return ["Error: Numbers must only contain digits.", True]
    else:
        return [None, False]


def lenOperation(operations):
    if len(operations) < 6:
        return [None, False]
    else:
        return ["Error: Too many problems.", True]


def calculate(signo, valorA=None, valorB=None, error=True):
    if error == True:
        if (signo != '+'):
            if (signo != '-'):
                return ["Error: Operator must be '+' or '-'", True]
        return [None, False]

    if signo == "+":
        return int(valorA) + int(valorB)
    elif signo == "-":
        return int(valorA) - int(valorB)


def dicCreator(data, dic):
    if True in data:
        dic["Error"] = data[0]
        return dic
    else:
        return dic


def Separador(operations):
    for i in operations:
        valorA, signo, valueB = i.split(" ")
        yield valorA, signo, valueB


def Errores(operations):
    dic = {}
    lisA = []
    lisB = []
    lisS = []
    dic = dicCreator(lenOperation(operations), dic)
    valores = Separador(operations)
    for valor in valores:
        dic = dicCreator(calculate(valor[1]), dic)
        dic = dicCreator(digitos(valor[0], valor[2]), dic)
        dic = dicCreator(lendigitos(valor[0], valor[2]), dic)
        if "Error" in dic:
            return True, dic, None
        else:
            lisA.append(valor[0])
            lisB.append(valor[2])
            lisS.append(valor[1])
    return lisA, lisB, lisS


def viewhola(valorA, valorB, Signo, view):
    pass


def arithmetic_arranger(operations, view=False):
    divA, divB, divS = Errores(operations)
    print(divA, divB, divS)
    pass


arithmetic_arranger(["32 + 698967", "3801 - 2", "45 + 43", "123 + 49"], False)
