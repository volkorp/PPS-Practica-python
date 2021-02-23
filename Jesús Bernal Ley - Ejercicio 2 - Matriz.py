# ENUNCIADO
# Generar una matriz 7 x 8 con números aleatorios y luego ordenarlo sin usar ningún tipo de librería o función predefinida.

# Ejercicio realizado por Jesús Bernal Ley

# Importamos la librería random para no tener que meter los datos contenidos en las matrices a mano:
from random import *

# Matriz a ordenar.
matriz = []

# Invoca las funciones que requiere el enunciado.
def main():
    generateRandoms()
    orderMatrix()


# Puebla la matriz 7x8 con números aleatorios del 0 al 99:
def generateRandoms():
    for row in range(7):
        matriz.append([randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99)])
    print('Matriz generada aleatoriamente:')
    printMatrix()

# Función para ordenar la matriz con el método de la burbuja.
def orderMatrix():
    # Variables de control: Tamaño de la matriz y fin del ciclo de iteraciones para su ordenación.
    rowLenght = len(matriz)
    columnLenght = 8
    isSorted = False

    # Método de la burbuja implementado.
    # Utiliza la variable "isSorted" para controlar si la matriz está ordenada o no.
    # El bucle tendrá que dar una iteración "en vacío" para confirmar que la matriz está completamente ordenada.
    while(not(isSorted)):        
        isSorted = True
        for row in range(rowLenght):
            for column in range(columnLenght):
                # Comprueba si el elemento que se está evaluando es el último de la matriz. Si es el caso, termina la ejecución.
                if(not(row == rowLenght - 1 and column == columnLenght - 1)):
                    row2 = row
                    column2 = column + 1

                # Salta a la siguiente línea si el elemento evaluado es el último de la fila.
                if(column2 == columnLenght):
                    row2 += 1
                    column2 = 0

                # Utilizando una variable temporal evalua dos elementos entre si y los intercambia si el primero es mayor que el segundo.
                # Actualiza la variable "isSorted" porque aún no podemos saber si la matriz está completamente ordenada.
                if(matriz[row][column] > matriz[row2][column2]):
                    temp = matriz[row][column]
                    matriz[row][column] = matriz[row2][column2]
                    matriz[row2][column2] = temp
                    isSorted = False
    print('Matriz oredenada:')
    printMatrix()

# Imprime la matriz:
def printMatrix():
    for row in matriz:
        print(row)


# Llamada al main:
if __name__ == "__main__":
    main()
