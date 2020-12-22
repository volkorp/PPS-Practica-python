print('Introduce 5 edades:')
loops = 0
entryList = []
userInput = 0
primos = []
nmax = 1000 # Número máximo de vueltas para calcular primos

# Entrada de datos
while loops < 5:
  try:
    userInput = int(input())
    entryList.append(userInput)
    loops+=1
  except:
    print('Debes insertar un número.')

print('Entendido')
# Cálculo menor
minValue = 0
firstLoop = 0

for inputs in entryList:
  if firstLoop == 0:
    minValue = inputs
    firstLoop+=1
  if inputs < minValue:
    minValue = inputs

# Cálculo mayor
maxValue = 0
firstLoop = 0

for inputs in entryList:
  if firstLoop == 0:
    maxValue = inputs
    firstLoop+=1
  if inputs > maxValue:
    maxValue = inputs

# Edades pares e impares
pairCount = 0
unevenCount = 0

for age in entryList:
  if age%2 == 0:
      pairCount+=1
  else:
      unevenCount+=1

# Primos
for numberChecked in entryList:
    for check in range(2, numberChecked):
        if(numberChecked%check != 0):
            continue
        else:
            break
    else:
        primos.append(numberChecked)

# Factorial
idx = max(primos)
factorial = 1

while idx > 0:
  factorial*=idx
  idx-=1

print('Mayor age: ' + str(maxValue))
print('Menor age: ' + str(minValue))
print('Cantidad de edades pares: ' + str(pairCount))
print('Cantidad de edades impares: ' + str(unevenCount))
print('Lista de primos: ' + str(primos))
print('Mayor primo: ' + str(max(primos)))
print('Factorial del mayor primo: ' + str(factorial))
