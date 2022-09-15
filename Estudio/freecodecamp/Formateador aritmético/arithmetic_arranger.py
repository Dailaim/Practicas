def comparador(listA, listB):
    """Esta funcion toma dos listas cadenas de strings del mismo tamaño y 
        compara cada una de sus indices para encontrar el mayor creando un 
        una nueva lista con los resultados

    Args:
        listA (Lista de strings): _description_
        listB (Lista de strings): _description_

    Returns:
        Lista de strings: Lista de el mayor numero de caracteres de las listas de entrada
    """

    
    salida = []
    for i in range(len(listA)):
        Entrada = []
        Entrada.append(len(listA[i]))
        Entrada.append(len(listB[i]))
        salida.append(max(Entrada))
    return salida


def lendigitos(valorA, valorB): 
    """Esta funcion se encarga de revisar que cada string no sea mayor a 4 caracteres

    Args:
        valorA (strings): _description_
        valorB (strings): _description_

    Returns:
        Lista: retorna se hay un Error o no con dos valores el primero es el error y 
        es un booleano que verifica al programador que hay un error
    """

    if len(valorA) < 5 and len(valorB) < 5:
        return [None, False]
    else:
        return ["Error: Numbers cannot be more than four digits.", True]


def digitos(valorA, valorB):
    """_summary_

    Args:
        valorA (_type_): _description_
        valorB (_type_): _description_

    Returns:
        _type_: _description_
    """
    validar = [None, None]
    validar[0] = valorA.isdigit()
    validar[1] = valorB.isdigit()
    if False in validar:
        return ["Error: Numbers must only contain digits.", True]
    else:
        return [None, False]


def lenOperation(operations):
    """_summary_

    Args:
        operations (_type_): _description_

    Returns:
        _type_: _description_
    """
    if len(operations) < 6:
        return [None, False]
    else:
        return ["Error: Too many problems.", True]
    
def ErrorSigno(valorS):
    if (valorS != '+'):
            if (valorS != '-'):
                return ["Error: Operator must be '+' or '-'.", True]
    return [None, False]


def calculate(listS, listA, listB):
    """Toma tres litas y va a determinar si hay que hacer una suma o una resta

    Args:
        listS (Lista de strings que contiene el signo ): Lista de los signos
        listA (Lista de strings con numeros): Lista de uno de los operandos
        listB (Lista de strings con numeros): Lista de uno de los operandos

    Returns:
        Regresa una lista con el todos los resutaldos de cada una de las operaciones 
    """
    listR=[]
    for i in range(len(listA)):
        if listS[i] == "+":
            result = str(int(listA[i]) + int(listB[i]))
        elif listS[i] == "-":
            result = str(int(listA[i]) - int(listB[i]))
        listR.append(result)
    return listR


def dicCreator(data, dic):
    """_summary_

    Args:
        data (_type_): _description_
        dic (_type_): _description_

    Returns:
        _type_: _description_
    """
    if True in data:
        dic["Error"] = data[0]
        return dic
    else:
        return dic


def Separador(operations):
    """Esta funcion se encarga de seprar por espacion una cadena de strings
        minimo debe tener dos espacion o no funcionara

    Args:
        operations (Lista de strings): formato ["a - b"] 

    Yields:
        Generador de tuplas : Genera una tupla en cada iteracion con los valores de cada uno de los 
        de la lista de entrada 
    """
    for i in operations:
        valorA, signo, valorB = i.split(" ")
        yield valorA, signo, valorB


def Errores(operations):
    """_summary_

    Args:
        operations (_type_): _description_

    Returns:
        _type_: _description_
    """
    dic = {}
    lisA = []
    lisB = []
    lisS = []
    dic = dicCreator(lenOperation(operations), dic)
    valores = Separador(operations)
    for valor in valores:
        dic = dicCreator(ErrorSigno(valor[1]), dic)
        dic = dicCreator(digitos(valor[0], valor[2]), dic)
        dic = dicCreator(lendigitos(valor[0], valor[2]), dic)
        if "Error" in dic:
            return True, dic, None
        else:
            lisA.append(valor[0])
            lisB.append(valor[2])
            lisS.append(valor[1])
    return lisA, lisB, lisS

def espaciosFinales(iteracion, lista):
    if not (iteracion == len(lista)-1):
            return "    "
    return ""



def viewhola(lisA, lisB, lisS, view=False):
    """Esta funcion se encarga de ordenar la farma de imprecion

    Args:
        lisA (Lista de strings numericos): Lista de uno de los operandos
        lisB (Lista de strings numericos): Lista de uno de los operandos
        lisS (Lista de strings): Esta lista solo puede tener "+" o "-"
        view (bool, optional): Esta define si decea visualizar el resultado de la operacion
    Returns:
        String: Forma en la que se visulizara el resultado
    """ 
    
    linea1 = linea2 = linea3 = linea4 = ""
    espacios = comparador(lisA, lisB)
    
    for i in range(len(espacios)):
        p = espacios[i]+2-len(lisA[i])
        linea1 += (" "*p + lisA[i])
        linea1 += espaciosFinales(i, espacios)
        
    for i in range(len(espacios)):
        p = espacios[i]+1-len(lisB[i])
        linea2 += (lisS[i] + " "*p + lisB[i])
        linea2 += espaciosFinales(i, espacios)
        
    for i in range(len(espacios)):
        linea3 += ("-"*(espacios[i]+2))
        linea3 += espaciosFinales(i, espacios)
        
        
    if view== True:
        lisR = calculate(lisS, lisA, lisB)
        for i in range(len(espacios)):
            p = espacios[i]+2-len(lisR[i])
            linea4+= (" "*p + lisR[i])
            linea4 += espaciosFinales(i, espacios)
        return linea1 + '\n' + linea2 + '\n' + linea3 + '\n' + linea4
            
    return linea1 + '\n' + linea2 + '\n' + linea3



def arithmetic_arranger(operations, view=False):
    """Esta funcion ejecuta la primera instancia del codigo y define si hay un error o no el mismo
        para realizar la imprecion de las opereciones

    Args:
        operations (Lista de strings): Esta lista contiene resive los valores para hacer las opereciones
        view (bool, optional): Esta define si decea visualizar el resultado de la operacion. Defaults to False.
    """
    lisA, lisB, lisS = Errores(operations)
    if lisA==True:
        return lisB["Error"]
    else:
        return viewhola(lisA, lisB, lisS, view)



print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))

