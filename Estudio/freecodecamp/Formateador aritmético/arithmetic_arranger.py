
def lendigitos(valorA, valorB):
    
    if  len(valorA) <5 or len(valorB) <5 :
        pass
    else:
        return ("Error: Numbers cannot be more than four digits.", True)
    


def digitos(valorA, valorB):
    validar= []
    validar[0] = valorA.isdigit()
    validar[1] = valorB.isdigit()
    if False in validar:
        return ("Error: Numbers must only contain digits.", True)

def lenOperation(operations):
    if len(operations) <6:
        pass
    else:
        return ("Error: Too many problems.", True)


def calculate(valorA, valorB, signo):
    if signo == "+":
        return int(valorA) + int(valorB)
    elif signo == "-":
        return int(valorA) - int(valorB)
    else:
        return ("Error: Operator must be '+' or '-'", True)
    
    
def Separador(operations):
    for i in operations:
        valorA, signo ,valueB = i.split(" ")
        yield valorA, signo ,valueB
    pass
    
def Errores(operations):
    
    
    pass


def arithmetic_arranger(operations, view=False):
    
    
    pass


print(calculate("456", "1223", "-"))

habla = Separador(["32 + 698"])
print(next(habla))

