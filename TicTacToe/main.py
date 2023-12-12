matriz = []

for i in range(3):
    matriz.append([0]*3)

#print(matriz)

contador = 0
condicion = True
repetido = False
ganar=False

print("  |   |")
print(matriz[0][0],"|",matriz[0][1],"|",matriz[0][2],"")
print("__|___|__")
print("  |   |")
print(matriz[1][0],"|",matriz[1][1],"|",matriz[1][2],"")
print("__|___|__")
print("  |   |")
print(matriz[2][0],"|",matriz[2][1],"|",matriz[2][2],"")
print("  |   |")


def ganarHorizontal(ficha):
    for i in range(3):
        contador=0
        for j in range(3):
            
            if matriz[i][j]==ficha:
                contador=contador + 1
        if contador == 3:
            return True
        
    return False

def ganarVertical(ficha):
    for i in range(3):
        contador=0
        for j in range(3):

            if matriz [j][i] == ficha:
                contador=contador + 1
        if contador == 3:
            return True
        
    return False

def ganarDiagonaldeIzqADer(ficha):
    contador = 0
    for i in range(3):
        if matriz[i][i]==ficha:
            contador = contador + 1
    if contador == 3:
        return True
    else: 
        return False
    
def ganarDiagonaldeDerAIzq(ficha):
    contador = 0
    for i in range(3):  
        if matriz[i][2-i] == ficha:
            contador = contador + 1
    if contador == 3:
        return True
    return False

while condicion and ganar==False:

    print("Jugador 1")
    while True:
        player1 = input("Elige donde anotar (1-9): ")
        if player1.isdigit() and 1 <= int(player1) <= 9:
            break
        else:
            print("Ingresa un número válido del 1 al 9. Intenta de nuevo.")
    #print("Jugador 1")
    #player1 = input("Elige donde anotar: ")

    if player1 == "1":
        if matriz[0][0] == "X":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        elif matriz[0][0] == "O":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        else:   
            matriz[0][0] = "O"
            
    
    if player1 == "2":
        if matriz[0][1] == "X":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        elif matriz[0][1] == "O":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        else:   
            matriz[0][1] = "O"

    if player1 == "3":
        if matriz[0][2] == "X":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        elif matriz[0][2] == "O":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        else:   
            matriz[0][2] = "O"

    if player1 == "4":
        if matriz[1][0] == "X":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        elif matriz[1][0] == "O":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        else:   
            matriz[1][0] = "O"
    
    if player1 == "5":
        if matriz[1][1] == "X":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        elif matriz[1][1] == "O":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        else:   
            matriz[1][1] = "O"

    if player1 == "6":
        if matriz[1][2] == "X":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        elif matriz[1][2] == "O":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        else:   
            matriz[1][2] = "O"

    if player1 == "7":
        if matriz[2][0] == "X":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        elif matriz[2][0] == "O":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        else:   
            matriz[2][0] = "O"
    
    if player1 == "8":
        if matriz[2][1] == "X":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        elif matriz[2][1] == "O":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        else:   
            matriz[2][1] = "O"

    if player1 == "9":
        if matriz[2][2] == "X":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        elif matriz[2][2] == "O":
            print("Este lugar ya esta ocupado, elige otro")
            repetido = True
        else:   
            matriz[2][2] = "O"
    
    print("  |   |")
    print(matriz[0][0],"|",matriz[0][1],"|",matriz[0][2],"")
    print("__|___|__")
    print("  |   |")
    print(matriz[1][0],"|",matriz[1][1],"|",matriz[1][2],"")
    print("__|___|__")
    print("  |   |")
    print(matriz[2][0],"|",matriz[2][1],"|",matriz[2][2],"")
    print("  |   |")

    if repetido == True:
        condicion = True
        repetido =False
    else:
        condicion = False

    ganar=ganarHorizontal("O") or ganarVertical("O") or ganarDiagonaldeIzqADer("O") or ganarDiagonaldeDerAIzq("O")

    if ganar == True:
        print("Jugador 1 ganó")
        break

    contador +=1

    if ganar == False and contador == 9 :
       # ganar==True
        print("Hubo un empate")
        break
    


    while condicion == False and ganar == False :
        print("Jugador 2")
        while True:
            player2 = input("Elige donde anotar (1-9): ")
            if player2.isdigit() and 1 <= int(player2) <= 9:
               break
            else:
                print("Ingresa un número válido del 1 al 9. Intenta de nuevo.")

        if player2 == "1":
            if matriz[0][0] == "O":
                print("Este lugar ya esta ocupado, elige otro")
                repetido = True
            elif matriz[0][0] == "X":
                print("Este lugar ya esta ocupado, elige otro")
            else:   
                matriz[0][0] = "X"
    
        if player2 == "2":
            if matriz[0][1] == "O":
                print("Este lugar ya esta ocupado, elige otro")
                repetido = True
            elif matriz[0][1] == "X":
                print("Este lugar ya esta ocupado, elige otro")
            else:   
                matriz[0][1] = "X"

        if player2 == "3":
            if matriz[0][2] == "O":
                print("Este lugar ya esta ocupado, elige otro")
                repetido = True
            elif matriz[0][2] == "X":
                print("Este lugar ya esta ocupado, elige otro")
            else:   
               matriz[0][2] = "X"

        if player2 == "4":
            if matriz[1][0] == "O":
                print("Este lugar ya esta ocupado, elige otro")
                repetido = True
            elif matriz[1][0] == "X":
                print("Este lugar ya esta ocupado, elige otro")
            else:   
                matriz[1][0] = "X"
    
        if player2 == "5":
            if matriz[1][1] == "O":
                print("Este lugar ya esta ocupado, elige otro")
                repetido = True
            elif matriz[1][1] == "X":
                print("Este lugar ya esta ocupado, elige otro")
            else:   
                matriz[1][1] = "X"

        if player2 == "6":
            if matriz[1][2] == "O":
                print("Este lugar ya esta ocupado, elige otro")
                repetido = True
            elif matriz[1][2] == "O":
                print("Este lugar ya esta ocupado, elige otro")
            else:   
                matriz[1][2] = "X"

        if player2 == "7":
            if matriz[2][0] == "O":
               print("Este lugar ya esta ocupado, elige otro")
               repetido = True
            elif matriz[2][0] == "X":
                print("Este lugar ya esta ocupado, elige otro")
            else:   
                matriz[2][0] = "X"
    
        if player2 == "8":
            if matriz[2][1] == "O":
                print("Este lugar ya esta ocupado, elige otro")
                repetido = True
            elif matriz[2][1] == "X":
                print("Este lugar ya esta ocupado, elige otro")
            else:   
                matriz[2][1] = "X"

        if player2 == "9":
            if matriz[2][2] == "O":
                print("Este lugar ya esta ocupado, elige otro")
                repetido = True
            elif matriz[2][2] == "X":
                print("Este lugar ya esta ocupado, elige otro")
            else:   
                matriz[2][2] = "X"
    
        print("  |   |")
        print(matriz[0][0],"|",matriz[0][1],"|",matriz[0][2],"")
        print("__|___|__")
        print("  |   |")
        print(matriz[1][0],"|",matriz[1][1],"|",matriz[1][2],"")
        print("__|___|__")
        print("  |   |")
        print(matriz[2][0],"|",matriz[2][1],"|",matriz[2][2],"")
        print("  |   |")
        if repetido == True:
            condicion = False
            repetido = False
        else:
            condicion = True

        ganar=ganarHorizontal("X") or ganarVertical("X") or ganarDiagonaldeIzqADer("X") or ganarDiagonaldeDerAIzq("X")
        if ganar == True:
            print("Jugador 2 ganó")
            break
        
        contador += 1  # Incrementa el contador después del movimiento del jugador 2

        if ganar == False and contador == 9:
            print("Hubo un empate")
            break



    



    
