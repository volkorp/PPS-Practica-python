# ENUNCIADO
# Hacer un programa en Python que permita almacenar en un fichero las temperaturas máximas y
# mínimas de las distintas provincias de Andalucía durante los días de la borrasca Filomena.
# Una vez almacenados el programa permitirá consultar la temperatura máxima y mínima de una provincia en un determinado día.

# Ejercicio realizado por Jesús Bernal Ley

import json
import datetime

data = {}
provinces = ['cadiz', 'malaga', 'huelva', 'sevilla', 'cordoba', 'jaen', 'almeria']

def main():
    promptUser()

def promptUser():
    print('-------------------------\nBienvenido a TempAnalyzer\n-------------------------')
    print('Opciones (inserta un número para continuar):\n 1. Añadir datos de provincia\n 2. Consultar datos de provincia\n 0. Salir del programa')
    try:
        userInput = int(input())
    except:
        print('Debes insertar un número.')

    if(userInput == 1):
        writeFile()
    if(userInput == 2):
        readFile()
    if(userInput == 0):
        print('¡Gracias, vuelva pronto!')


def readFile():
    notValid = True

    # Valida si la provincia introducida es válida
    print('¿Qué provincia te gustaría consultar? (nombre de provincia andaluza)')
    while notValid:
        userInput = input().lower()
        if userInput not in provinces:
            print('Debes especificar una provincia de Andalucía')
        else:
            notValid = False
    
    # Lee el fichero
    with open('data.json', 'r') as myfile:
        data = myfile.read()

    # Formatea a objeto json los datos del archivo
    obj = json.loads(data)

    try:
        print('-------------------------')
        # Muestra los registros de la provincia especificada
        for item in obj[userInput]:
            print('Fecha: ' + item['fecha'])
            print('Temperatura máxima: ' + item['max'])
            print('Temperatura mínima: ' + item['min'] + '\n')
    except:
        print('No existen registros de la provincia indicada.\n\n')
    
    # Vuelve al bucle de menú
    promptUser()


def writeFile():
    # Variable de control para formatos
    notValid = True

    # Valida si la provincia introducida es válida
    print('¿Para qué provincia quieres añadir el nuevo registro?')
    while notValid:
        province = input().lower()
        if province not in provinces:
            print('Debes especificar una provincia de Andalucía')
        else:
            notValid = False
    notValid = True

    # Pide la fecha y valida su formato
    print('¿Qué fecha quieres añadir? (dd/mm/aaaa)')
    while notValid:        
        try:
            date = input().lower()
            datetime.datetime.strptime(date, '%d/%m/%Y')
            notValid = False
        except ValueError:
            print('Formato inválido, debe ser: dd/mm/aaaa')
    notValid = True

    # Pide la temperatura máxima y validad si es un número
    print('¿Qué temperatura máxima hubo ese día?')
    while notValid:
        try:
            max = int(input())
            notValid = False
        except:
            print('Debes insertar un número.')
    notValid = True

    # Pide la temperatura mínima y validad si es un número
    print('¿Qué temperatura mínima hubo ese día?')
    while notValid:
        try:
            min = int(input())
            notValid = False
        except:
            print('Debes insertar un número.')

    # Solo añade la provincia si no existe ningún registro anterior:
    if(province not in data):
        data[province] = []

    # Añade el registro a una provincia existente:
    data[province].append({
        'fecha': date,
        'max': str(max),
        'min': str(min)
    })

    # Vuelca en el fichero los datos del json
    with open('data.json', 'w') as dataFile:
        json.dump(data, dataFile)

    # Vuelve al bucle de menú
    promptUser()

# Llamada al main:
if __name__ == "__main__":
    main()
