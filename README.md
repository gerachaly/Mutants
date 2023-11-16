# Mutants
Parcial 2 Programacion: Mutants
* Nombre y Apellido: Gerardo Gomez
* Legajo: 51560
* Email: geracreepy14@gmail.com

## De que va el proyecto

El proyecto se basa en el reclutamiento de Mutantes para la pelea contra los X-Men's, para eso se pide una lista de cadenas de ADN, verificando que si tiene secuencias repetitivas, indicando ser un mutante.

### Como Funciona

Primero se le pide al usuario que siga unos pasos para ingresar su secuencia de ADN, verificando que ingrese 6 digitos y que no ingrese numeros.

```
while len(SecuenciaADN) < 6:
    print("Secuencia {}: ".format(len(SecuenciaADN)+1), end=" ")
    entrada = input()
    # ... verificadores

```
Luego se crea una variable de tipo bool donde se llama a una funcion que imprime la secuencia de ADN como matriz bidimensional.

```
resultado = isADN(SecuenciaADN)
```

```
def isADN(secuencia):
    # ... logica de impresion de la secuencia
    esMutante = recorrerADN(secuencia)
    return esMutante
```

Dentro de esa funcion se llama a otra funcion donde se retorna el resultado booleano, para verificar si es mutante o no.
Recorriendo horizontal, vertical y oblicuo la matriz.

```
def recorrerADN(secuencia):
    contador = 0 # se inicializa un contador

    # logica de recorrido horizontal
    if ... :
        contador+=1

    # logica de recorrido vertical
    transpuesta = list(map(list, zip(*secuencia))) 
    # zip hace que traspuesta tenga los valores de cada columna de la secuencia
    if ... :
        contador+=1

    # logica de recorrido oblicuo
    if ... :
        contador+=1

    #logica de recorrido oblicuo traspuesto
    if ... :
        contador+=1

    return contador > 2 
        # retorna true si contador > 2, caso contrario falso.
```

Terminando con un print

```
resultado = isADN(SecuenciaADN)

if resultado:
    print("Felicidades, es mutante!!")
    print("Ahora puede pelear contra el pelado en la silla de ruedas.")
else:
    print("Lo sentimos, usted es cualquier cosa menos mutante.")
```

## Como correrlo

Primero se tiene que hacer clone del resositorio 
```
git clone https://github.com/gerachaly/Mutants.git
```
Luego por consola accedemos a el
```
cd Mutants
```
Luego ejecutamos el archivo python TPMutants.py
Y hacerle caso a las consignas del codigo