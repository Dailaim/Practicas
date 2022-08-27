import random


def printIntro(introFile):
    '''
        Firma:
            (string) -> ()

        Sinopsis:
            función que imprime el contenido de un archivo en pantalla, en este
                caso, el mensaje de bienvenida al juego

        Entradas y salidas:
            - inputFile: Nombre del archivo que contiene la presentación del juego
            - returns: None, solo imprime el archivo leído en pantalla

        Ejemplos de uso:

            >>> printIntro("intro.txt")

            ████████╗██████╗ ██╗ ██████╗ ██╗   ██╗██╗
            ╚══██╔══╝██╔══██╗██║██╔═══██╗██║   ██║██║
               ██║   ██████╔╝██║██║   ██║██║   ██║██║
               ██║   ██╔══██╗██║██║▄▄ ██║██║   ██║██║
               ██║   ██║  ██║██║╚██████╔╝╚██████╔╝██║
               ╚═╝   ╚═╝  ╚═╝╚═╝ ╚══▀▀═╝  ╚═════╝ ╚═╝
        '''

    # Desarrolle el cuerpo de la función aquí...
    x = open(introFile, encoding="utf8")
    print(x.read())
    pass


def drawBoard(board):
    # Esta función imprime el tablero en la consola
    # in Argumentos:
    # Board: Lista de strings que representa el estado del tablero

    # Desarrolle el cuerpo de la función aquí...
    cont = 7

    for fila in range(3):
        print(" ", end="")
        for columna in range(2):
            print(board[cont], "| ", end="")
            cont = cont + 1
        print(board[cont])
        if (cont > 4):
            print("", "-", "+", "-", "+", "-")
        cont = cont - 5
    pass


def inputPlayerLetter():
    # Esta función le permite escoger al usuario entre la letra "X" y la letra "O".

    # retorna una lista de strings donde la letra escogida por el usuario
    # ocupa la primera posición y la letra que le corresponde a la computadora
    # ocupa la segunda posición.

    # Desarrolle el cuerpo de la función aquí...
    while True:
        jugador = input("Escoje entre la X o O: ")
        if (len(jugador) == 1):
            if (jugador.upper() == "X"):
                lista = ['X', 'O']
                return lista
            elif (jugador.upper() == "O"):
                lista = ['O', 'X']
                return lista
            else:
                print("El codigo solo acepta entre las opciones X o O.")
        else:
            print("EL juego solo acepta un valor y entre X o O.")
    pass


def whoGoesFirst():
    # Esta función escoge de forma aleatoria quien inicial el juego.
    # Retorna el string "Usuario" si el usuario inicia el juego o
    # el string "Computadora" si la computadora inicia el juego.

    # Desarrolle el cuerpo de la función aquí...

    if(int(random.random() * 2 - 1 + 1 + 1) == 1):
        return "Usuario"
    else:
        return "Computadora"


def makeMove(board, letter, move):
    # Esta función actualiza el estado del tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # letter: Es la marca que se desea poner en el tablero ("X" o "O").
    # move: Es el número de la casilla donde se desea poner la marca.

    # Desarrolle el cuerpo de la función aquí...

    board[move] = letter
    pass


def isWinner(board, letter):
    # Esta función debe verificar si hay una jugada ganadora en el tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # letter: La marca que se desea verificar ("X" o "O").

    # Esta función debe retornar el valor lógico True, si hay una jugada ganadora o
    # debe retornar el valor lógico False, si no hay una jugada ganadora.

    # Desarrolle el cuerpo de la función aquí...
    if (letter == board[1] and letter == board[2] and letter == board[3]):
        return True
    elif(letter == board[4] and letter == board[5] and letter == board[6]):
        return True
    elif(letter == board[7] and letter == board[8] and letter == board[9]):
        return True
    elif(letter == board[1] and letter == board[4] and letter == board[7]):
        return True
    elif(letter == board[2] and letter == board[5] and letter == board[8]):
        return True
    elif(letter == board[3] and letter == board[6] and letter == board[9]):
        return True
    elif(letter == board[1] and letter == board[5] and letter == board[9]):
        return True
    elif(letter == board[3] and letter == board[5] and letter == board[7]):
        return True
    else:
        return False


def isSpaceFree(board, move):
    # Esta función verifica si hay una casilla vacía en el tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # move: Es el número de la casilla que se desea verificar.

    # Esta función debe retornar el valor lógico True, si la casilla está vacía
    # en caso contrario, debe retornar el valor lógico False.

    # Desarrolle el cuerpo de la función aquí...
    if (board[move] == " "):
        return True
    else:
        return False
    pass


def getPlayerMove(board):
    # Esta función le pide al usuario que ingrese el número de la casilla
    # que quiere marcar.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.

    # Esta función retorna el número de la casilla seleccionada por el usuario.

    # Desarrolle el cuerpo de la función aquí...

    while True:
        print("Recuerda las casilla estan enumeradas del 1 al 9 de izquierda a derecha, de arriba pora abajo Y solo se permite marcar una casilla.")
        letter = input("Ingresa el valor de la casilla que deseas marcar: ")
        if (len(letter) == 1):
            if(letter.isnumeric()):
                letter = int(letter)
                if(0 < letter < 10):
                    if(isSpaceFree(board, letter)):
                        return letter
                    else:
                        print("Esta casilla ya esta marcada")
                        continue
        print("Valor incorrecto")

    pass


def chooseRandomMoveFromList(board, movesList):
    # Esta función escoge de forma aleatoria una casilla vacía del tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # moveList: Lista que contiene los números de las casillas a verificar (ver documento de la práctica).

    # Esta función debe retornar alguno de los números de casillas en moveList
    # desde que dicha casilla esté vacía. Si ninguna de las casillas está vacía,
    # esta función debe retornar el valor None.

    # Desarrolle el cuerpo de la función aquí...
    element = len(movesList)
    elementL = 0
    for i in movesList:
        if(isSpaceFree(board, i) == True):
            break
        else:
            elementL += 1
    if(elementL == element):
        return None
    while True:
        n = random.choice(movesList)
        if(isSpaceFree(board, n)):
            return n

    pass


def getComputerMove(board, computerLetter):
    # Esta función implementa la estrategia de juego de la computadora.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # computerLetter: La marca que está usando la computadora.

    # Desarrolle el cuerpo de la función aquí...

    # 1. Verificar si la computadora puede ganar...

    if(board[7] == computerLetter and board[8] == computerLetter and isSpaceFree(board, 9)):
        return 9
    if(board[7] == computerLetter and board[9] == computerLetter and isSpaceFree(board, 8)):
        return 8
    if(board[8] == computerLetter and board[9] == computerLetter and isSpaceFree(board, 7)):
        return 7
    if(board[4] == computerLetter and board[5] == computerLetter and isSpaceFree(board, 6)):
        return 6
    if(board[4] == computerLetter and board[6] == computerLetter and isSpaceFree(board, 5)):
        return 5
    if(board[5] == computerLetter and board[6] == computerLetter and isSpaceFree(board, 4)):
        return 4
    if(board[1] == computerLetter and board[2] == computerLetter and isSpaceFree(board, 3)):
        return 3
    if(board[1] == computerLetter and board[3] == computerLetter and isSpaceFree(board, 2)):
        return 2
    if(board[2] == computerLetter and board[3] == computerLetter and isSpaceFree(board, 1)):
        return 1
    if(board[7] == computerLetter and board[4] == computerLetter and isSpaceFree(board, 1)):
        return 1
    if(board[1] == computerLetter and board[4] == computerLetter and isSpaceFree(board, 7)):
        return 7
    if(board[7] == computerLetter and board[1] == computerLetter and isSpaceFree(board, 4)):
        return 4
    if(board[8] == computerLetter and board[5] == computerLetter and isSpaceFree(board, 2)):
        return 2
    if(board[8] == computerLetter and board[2] == computerLetter and isSpaceFree(board, 5)):
        return 5
    if(board[5] == computerLetter and board[2] == computerLetter and isSpaceFree(board, 8)):
        return 8
    if(board[9] == computerLetter and board[6] == computerLetter and isSpaceFree(board, 3)):
        return 3
    if(board[9] == computerLetter and board[3] == computerLetter and isSpaceFree(board, 6)):
        return 6
    if(board[6] == computerLetter and board[3] == computerLetter and isSpaceFree(board, 9)):
        return 9
    if(board[7] == computerLetter and board[5] == computerLetter and isSpaceFree(board, 3)):
        return 3
    if(board[7] == computerLetter and board[3] == computerLetter and isSpaceFree(board, 5)):
        return 5
    if(board[5] == computerLetter and board[3] == computerLetter and isSpaceFree(board, 7)):
        return 7
    if(board[9] == computerLetter and board[5] == computerLetter and isSpaceFree(board, 1)):
        return 1
    if(board[9] == computerLetter and board[1] == computerLetter and isSpaceFree(board, 5)):
        return 5
    if(board[5] == computerLetter and board[1] == computerLetter and isSpaceFree(board, 9)):
        return 9
    # 2. Si no, verificar si el usuario puede ganar en la siguiente jugada, si si, bloquear esta jugada...
    if(computerLetter == 'X'):
        letter = 'O'
    else:
        letter = 'X'
    if(board[7] == letter and board[8] == letter and isSpaceFree(board, 9)):
        return 9
    if(board[7] == letter and board[9] == letter and isSpaceFree(board, 8)):
        return 8
    if(board[8] == letter and board[9] == letter and isSpaceFree(board, 7)):
        return 7
    if(board[4] == letter and board[5] == letter and isSpaceFree(board, 6)):
        return 6
    if(board[4] == letter and board[6] == letter and isSpaceFree(board, 5)):
        return 5
    if(board[5] == letter and board[6] == letter and isSpaceFree(board, 4)):
        return 4
    if(board[1] == letter and board[2] == letter and isSpaceFree(board, 3)):
        return 3
    if(board[1] == letter and board[3] == letter and isSpaceFree(board, 2)):
        return 2
    if(board[2] == letter and board[3] == letter and isSpaceFree(board, 1)):
        return 1
    if(board[7] == letter and board[4] == letter and isSpaceFree(board, 1)):
        return 1
    if(board[1] == letter and board[4] == letter and isSpaceFree(board, 7)):
        return 7
    if(board[7] == letter and board[1] == letter and isSpaceFree(board, 4)):
        return 4
    if(board[8] == letter and board[5] == letter and isSpaceFree(board, 2)):
        return 2
    if(board[8] == letter and board[2] == letter and isSpaceFree(board, 5)):
        return 5
    if(board[5] == letter and board[2] == letter and isSpaceFree(board, 8)):
        return 8
    if(board[9] == letter and board[6] == letter and isSpaceFree(board, 3)):
        return 3
    if(board[9] == letter and board[3] == letter and isSpaceFree(board, 6)):
        return 6
    if(board[6] == letter and board[3] == letter and isSpaceFree(board, 9)):
        return 9
    if(board[7] == letter and board[5] == letter and isSpaceFree(board, 3)):
        return 3
    if(board[7] == letter and board[3] == letter and isSpaceFree(board, 5)):
        return 5
    if(board[5] == letter and board[3] == letter and isSpaceFree(board, 7)):
        return 7
    if(board[9] == letter and board[5] == letter and isSpaceFree(board, 1)):
        return 1
    if(board[9] == letter and board[1] == letter and isSpaceFree(board, 5)):
        return 5
    if(board[5] == letter and board[1] == letter and isSpaceFree(board, 9)):
        return 9
    # 3. Si no, tratar de poner una marca en alguna de las esquinas, si alguna está vacía...
    moveList = [7, 9, 1, 3]
    move = chooseRandomMoveFromList(board, moveList)
    if(move != None):
        return move
    # 4. Si no, tratar de marcar la casilla del centro, si esta está vacía...
    moveList = [5]
    move = chooseRandomMoveFromList(board, moveList)
    if(move != None):
        return move
    # 5. Si no, tratar de poner una marca en alguna de las casillas de los lados...
    moveList = [8, 4, 6, 2]
    move = chooseRandomMoveFromList(board, moveList)
    if(move != None):
        return move

    pass


def isBoardFull(board):
    # Esta función verifica si el tablero está lleno.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.

    # Esta función debe retorna el valor lógico True, si el tablero está lleno.
    # En caso contrario debe retornar el valor lógico False.

    # Desarrolle el cuerpo de la función aquí...
    if(" " in board):
        return False
    return True


def record(finalFile, player, pc, empate, name, fecha):
    x = open(finalFile, "a")
    print(x.write(("-"*10)+"triqui"+("-"*10)))
    print(x.write("\n"))
    print(x.write("\n"))
    print(x.write(fecha))
    print(x.write("\n"))
    print(x.write("\n"))
    print(x.write("nombre del jugador: "))
    print(x.write(name))
    print(x.write("\n"))
    print(x.write("\n"))
    print(x.write("Juegos ganados por el usurio - "))
    print(x.write(str(player)))
    print(x.write("\n"))
    print(x.write("Juegos ganados por la computadora - "))
    print(x.write(str(pc)))
    print(x.write("\n"))
    print(x.write("Juegos empatados - "))
    print(x.write(str(empate)))
    print(x.write("\n"))
    print(x.write("\n"))
    print(x.write("-"*26))
    print(x.write("\n"))
    x.close()
    return
