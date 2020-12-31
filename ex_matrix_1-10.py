
#1. Leer una matriz 4x4 entera y determinar en qué fila y en qué columna se encuentra el número
# mayor.
matriz = []
mayor = 0
multiplos8 = []
columna = 0
fila = 0
for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige números para la matriz: ")))
for i in range(4):
    for j in range(4):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
for i in range(4):
    fila = fila + 1
    columna = 0
    for j in range(4):
        columna = columna + 1
        if matriz[i][j] == mayor:
            print("Posicion del mayor número: Fila: " + str(fila) + ". Columna: " + str(columna) + ".")
            break

#2. Leer una matriz 4x4 entera y determinar cuántas veces se repita en ella el número mayor.
matriz = []
mayor = 0
contador = 0
for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige un número: ")))
for i in range(4):
    for j in range(4):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
for i in range(4):
    for j in range(4):
        if matriz[i][j] == mayor:
            contador = contador + 1
print("Cantidad de veces que se repite el número mayor: " + str(contador))

#3. Leer una matriz 3x4 entera y determinar en qué posiciones exactas se encuentran los números
# pares.
matriz = []
pares = []
fila = 0
columna = 0
for i in range(3):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige números para la matriz: ")))
for i in range(3):
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            pares.append(matriz[i][j])
print("Posiciones de los números pares: ")
for par in pares:
    fila = 0
    for i in range(3):
        fila = fila + 1
        columna = 0
        for j in range(4):
            columna = columna + 1
            if matriz[i][j] == par:
                print("Fila: " + str(fila) + ". Columna: " + str(columna) + ".")

#4. Leer una matriz 4x3 entera y determinar en qué posiciones exactas se encuentran los números
# primos.
matriz = []
primos = []
fila = 0
columna = 0
for i in range(4):
    matriz.append([])
    for j in range(3):
        matriz[i].append(int(input("Elige números para la matriz: ")))
for i in range(4):
    for j in range(3):
        for x in range(2, ((matriz[i][j]) - 1)):
            if int((matriz[i][j]) % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or matriz[i][j] == 2 or matriz[i][j] == 3:
            primos.append(matriz[i][j])
print("Posiciones de los números primos: ")
for primo in primos:
    fila = 0
    for i in range(4):
        fila = fila + 1
        columna = 0
        for j in range(3):
            columna = columna + 1
            if matriz[i][j] == primo:
                print("Fila: " + str(fila) + ". Columna: " + str(columna) + ".")

#5. Leer una matriz 4x3 entera, calcular la suma de los elementos de cada fila y determinar cuál es
# la fila que tiene la mayor suma.
matriz = []
suma = 0
sumas = []
contador = 0
for i in range(4):
    matriz.append([])
    for j in range(3):
        matriz[i].append(int(input("Elige un número: ")))
for i in range(4):
    suma = 0
    for j in range(3):
        suma = suma + matriz[i][j]
    sumas.append(suma)
mayor = sumas[0]
for sum in sumas:
    if sum > mayor:
        mayor = sum
for sum in sumas:
    contador = contador + 1
    if sum == mayor:
        break
print("Fila con la mayor suma de números: " + str(contador))

#6. Leer una matriz 4x4 entera y calcular el promedio de los números mayores de cada fila.
matriz = []
mayor = 0
mayores = []
suma = 0
promedio = 0
for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige números para la primera matriz: ")))
for i in range(4):
    mayor = 0
    for j in range(4):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
    mayores.append(mayor)
for number in mayores:
    suma = suma + number
promedio = int(suma / 4)
print("Promedio de los números mayores de cada fila: " +str(promedio))

#7. Leer una matriz 4x4 entera y determinar en qué posiciones están los enteros terminados en 0.
matriz = []
termina_cero = []
fila = 0
columna = 0
for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige números para la matriz: ")))
for i in range(4):
    for j in range(4):
        if matriz[i][j] % 10 == 0:
            termina_cero.append(matriz[i][j])
print("Posiciones de los números terminados en cero: ")
for number in termina_cero:
    fila = 0
    for i in range(4):
        fila = fila + 1
        columna = 0
        for j in range(4):
            columna = columna + 1
            if matriz[i][j] == number:
                print("Fila: " + str(fila) + ". Columna: " + str(columna) + ".")

#8. Leer una matriz 4x4 entera y determinar cuántos enteros terminados en 0 hay almacenados en
# ella.
matriz = []
contador = 0
cero = []
for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige un número: ")))

for i in range(4):
    for j in range(4):
        if int((matriz[i][j]) % 10) == 0:
            contador = contador + 1
print("Cantidad de números terminados en 0 en la matriz: " + str(contador))

#9. Leer una matriz 3x4 entera y determinar cuántos de los números almacenados son primos y
# terminan en 3.
matriz = []
contador = 0
for i in range(3):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige un número: ")))
for i in range(3):
    for j in range(4):
        for x in range(2, (matriz[i][j] - 1)):
            if int(matriz[i][j] % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True and int(matriz[i][j] % 10) == 3:
            contador = contador + 1
print("Cantidad de números primos terminados en 3: " + str(contador))

#10. Leer una matriz 5x3 entera y determinar en qué fila está el mayor número primo.
matriz = []
mayor = 0
primos = []
posicion = 0
contador = 0
is_prime = False
for i in range(5):
    matriz.append([])
    for j in range(3):
        matriz[i].append(int(input("Elige números para la primera matriz: ")))
for i in range(5):
    for j in range(3):
        for x in range(2, (matriz[i][j] - 1)):
            if int(matriz[i][j] % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or matriz[i][j] == 2 or matriz[i][j] == 3:
            primos.append(matriz[i][j])
mayor = primos[0]        
for primo in primos:
    if primo > mayor:
        mayor = primo
for i in range(4):
    for j in range(3):
        contador = contador + 1
        if matriz[i][j] == mayor:
            posicion = int(contador / 3) + 1
            print("Fila en la que esta el mayor número primo: " + str(posicion))
            break
