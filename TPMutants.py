print("Bienvenido al reclutamiento de Mutantes!")
print("Queremos probar su valentia y coraje para pelear contra los X-Men's")
print("Le pido porfacor que ingrese su secuencia de ADN de longitud 6(A, T, C, G)")
print("Ejemplo 'CGATTC")
print("(En MAYUSCULAS)")
letrasValidas = "ATCG"
SecuenciaADN = []

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

def valida_letras(entrada, letras):
    for car in entrada:
        if car not in letras:  ## Funcion que valida si la secuencia contiene las letras A,T,C,G
            return False       ## si contiene otras letras devuelve falso.
    return True