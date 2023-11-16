print("Bienvenido al reclutamiento de Mutantes!")
print("Queremos probar su valentia y coraje para pelear contra los X-Men's")
print("Le pido porfacor que ingrese su secuencia de ADN de longitud 6(A, T, C, G)")
print("Ejemplo 'CGATTC")
print("(En MAYUSCULAS)")
letrasValidas = "ATCG"
SecuenciaADN = []


def valida_letras(entrada, letras):
    for car in entrada:
        if car not in letras:  ## Funcion que valida si la secuencia contiene las letras A,T,C,G
            return False       ## si contiene otras letras devuelve falso.
    return True


def isADN(secuencia): ##esta funcion lo que hace es imprimir toda la secuencia de adn
    esMutante = None    ## el llamado a la otra funcion es para recorrer el adn.
    for filas in SecuenciaADN:
        print("|",end="")
        for col in filas:
            print(col, end = "|")
        print("")
    esMutante = recorrerADN(secuencia)
    return esMutante

def recorrerADN(secuencia): ## en esta funcion recorre horizontal, vertical, y ambas partes oblicuas 
    contador = 0                ## para detectar si hay secuencias de adn o no
    for filas in secuencia:
        for col in range(len(filas)-3):
            if filas[col] == filas[col+1] == filas[col+2] == filas[col+3]:  ## horizontal
                contador+=1

    transpuesta = list(map(list, zip(*secuencia)))

    for col in transpuesta:
        for fila in range(len(col)-3):
            if col[fila] == col[fila+1] == col[fila+2] == col[fila+3]:      ## vertical
                contador+=1

    for i in range(len(secuencia)-3):
        for j in range(len(secuencia[0])-3):
            if secuencia[i][j] == secuencia[i+1][j+1] == secuencia[i+2][j+2] == secuencia[i+3][j+3]: ##diagonal
                contador+=1

    for i in range(len(secuencia)-3):
        for j in range(3, len(secuencia[0])):
            if secuencia[i][j] == secuencia[i+1][j-1] == secuencia[i+2][j-2] == secuencia[i+3][j-3]: ## diagonal traspuesta
                contador+=1
    
    return contador >=2 ## devuelve true si el contador es 2 o mas, o false si el contador es menor a 2

while len(SecuenciaADN) < 6:
    print("Secuencia {}: ".format(len(SecuenciaADN)+1), end=" ")
    entrada = input()
    if len(entrada) !=6:
        print("La secuencia tiene que tener solo 6 digitos.") ## aca se pide la secuencia de adn en forma de string
    elif entrada.isdigit():                                   ## y se hacen las validaciones de no tener numeros y ser mayor a 6 digitos.
        print("Error, la secuencia no puede tener numeros")
    elif valida_letras(entrada, letrasValidas):
        SecuenciaADN.append(list(entrada.upper()))
    else:
        print("La secuencia solo puede contener las letras (A, T, C, G).")

resultado = isADN(SecuenciaADN)

if resultado:       ## aca dependiendo el resultado es lo que dira.
    print("Felicidades, es mutante!!")
    print("Ahora puede pelear contra el pelado en la silla de ruedas.")
else:
    print("Lo sentimos, usted es cualquier cosa menos mutante.")