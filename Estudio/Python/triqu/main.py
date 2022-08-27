import datetime
import triqui as tr

# 1. Mostrar mensaje de bienvenida
tr.printIntro('intro.txt')
# Indica quién tiene el turno para jugar, el usuario o la computadora.
turn = ""
letterGame = ""
pc = 0
player = 0
empate = 0
guardado = ""
while True:

    # 2. Crear el tablero
    board = [None, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # 3. El usuario debe seleccionar la marca
    letterGame = tr.inputPlayerLetter()
    # 4. Quién va primero el usuario o la computadora?
    turn = tr.whoGoesFirst()

    print(turn + ' va primero.')

    jugando = True  # El juego ha iniciado

    while jugando:
        if turn == 'Usuario':  # 5. Turno del usuario

            # a. Mostrar tablero
            tr.drawBoard(board)
            # b. Pedir jugada al usuario
            move = tr.getPlayerMove(board)
            # c. Actualizar el tablero
            tr.makeMove(board, letterGame[0], move)
            # d. Verificar si el usuario ha ganado el juego.
            result = tr.isWinner(board, letterGame[0])
            #    Si si, mostrar tablero, mostrar mensaje de felicitación y terminar el juego.
            if(result == True):
                tr.drawBoard(board)
                print("Felicitaciones, has ganado el juego!")
                player = player + 1
                break
            # e. Verificar si hay empate.
            result = tr.isBoardFull(board)
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.
            if(result == True):
                tr.drawBoard(board)
                print("Juego empatado!")
                empate = empate + 1
                break
            # f. Si el usuario no ha ganado y no hay empate, la computadora
            #    toma el siguiente turno

            turn = 'Computadora'

        else:  # 6. Turno de la computadora.

            # a. Computadora hace jugada.
            move = tr.getComputerMove(board, letterGame[1])
            # b. Actualizar el tablero.
            tr.makeMove(board, letterGame[1], move)
            # c. Verificar si la computadora ha ganado el juego.
            result = tr.isWinner(board, letterGame[1])
            #    Si si, mostrar tablero, mostrar mensaje indicando al usuario que ha perdido y terminar el juego.
            if(result == True):
                tr.drawBoard(board)
                print("La computadora te ha vencido! Perdiste")
                pc = pc + 1
                break
            # d. Verificar si hay empate.
            result = tr.isBoardFull(board)
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.
            if(result == True):
                tr.drawBoard(board)
                print("Juego empatado!")
                empate = empate + 1
                break
            # f. Si la computadora no ha ganado y no hay empate, el usuario
            #    toma el siguiente turno.

            turn = 'Usuario'

    # 7. Preguntar si el usuario quiere jugar una vez mas
    result = ""
    while((result == "no" or result == "si") == False):
        result = input("¿Quieres Jugar de Nuevo? (Si - No)\n")
        result = result.lower()
        if(result != "no" and result != "si"):
            print("El programa solo acepta los valores si y no.")
    #    Si no, finalizar el programa.
    if(result == "no"):
        while((guardado == "no" or guardado == "si") == False):
            guardado = input("¿Quieres guardar tus resultados? (Si - No)\n")
            guardado = guardado.lower()
            if(guardado == "si"):
                ahora = datetime.datetime.now()
                ahora = ahora.strftime("%c")
                name = input("Cual es tu nombre: ")
                tr.record("log.txt", player, pc, empate, name, ahora)
                break
            elif(guardado == "no"):
                break
            else:
                print("El programa solo acepta los valores si y no.")
        break
