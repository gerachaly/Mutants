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
 Luego