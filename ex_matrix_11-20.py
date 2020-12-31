
#11. Leer una matriz 5x3 entera y determinar en qué columna está el menor número par.
matriz = []
menor = 0
pares = []
columna = 0
for i in range(5):
    matriz.append([])
    for j in range(3):
        matriz[i].append(int(input("Elige números para la matriz: ")))
for i in range(5):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            pares.append(matriz[i][j])
menor = pares[0]
for par in pares:
    if par < menor:
        menor = par
for i in range(5):
    columna = 0
    for j in range(3):
        columna = columna + 1
        if matriz[i][j] == menor:
            print("Columna del menor número par: " + str(columna) + ".")

#12. Leer una matriz 5x5 entera y determinar en qué fila está el mayor número terminado en 6.
matriz = []
mayor = 0
mayores = []
mayor_seis = 0
contador = 0
for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(int(input("Elige números para la primera matriz: ")))
for i in range(5):
    mayor = 0
    for j in range(5):
        if matriz[i][j] > mayor and matriz[i][j] % 10 == 6:
            mayor = matriz[i][j]
    mayores.append(mayor)
mayor_seis = mayores[0]
for number in mayores:
    if number > mayor_seis:
        mayor_seis = number
for number in mayores:
    contador = contador + 1
    if number == mayor_seis:
        break
print("Fila donde esta el mayor número terminado en 6: " + str(contador))

#13. Leer una matriz 5x3 entera y determinar en qué columna está el mayor número que comienza
# con el dígito 4.
matriz = []
cuatros = []
columna = 0
for i in range(5):
    matriz.append([])
    for j in range(3):
        matriz[i].append(int(input("Elige números para la matriz: ")))
for i in range(5):
    for j in range(3):
        x = matriz[i][j]
        while x >= 10:
            x = int(x / 10)
        if x == 4:
            cuatros.append(matriz[i][j])
mayor = 0
for cuatro in cuatros:
    if cuatro > mayor:
        mayor = cuatro    
if mayor == 0:
    print("En la matriz no hay números que empiecen por 4.")
for i in range(5):
    columna = 0
    for j in range(3):
        columna = columna + 1
        if matriz[i][j] == mayor:
            print("El número más grande que empieza por 4 esta en la columna: " + str(columna) + ".")
            break

#14. Leer una matriz 5x5 entera y determinar cuántos números almacenados en ella tienen mas de
# 3 dígitos.
matriz = []
contador = 0
for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(int(input("Elige un número: ")))
for i in range(5):
    for j in range(5):
        if matriz[i][j] >= 1000:
            contador = contador + 1
print("Cantidad de números con más de tres dígitos: " + str(contador))

#15. Leer una matriz 5x4 entera y determinar cuántos números almacenados en ella terminan en
# 34.
matriz = []
contador = 0
for i in range(5):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige un número: ")))
for i in range(5):
    for j in range(4):
        if int(matriz[i][j] % 100) == 34:
            contador = contador + 1
print("Cantidad de números que terminan en 34: " + str(contador))

#16. Leer una matriz 5x4 entera y determinar cuántos números almacenados en ella tienen un solo
# dígito.
matriz = []
contador = 0
for i in range(5):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige un número: ")))
for i in range(5):
    for j in range(4):
        if matriz[i][j] >= -9 and matriz[i][j] <= 9:
            contador = contador + 1
print("Cantidad de números con un solo dígito: " + str(contador))

#17. Leer una matriz 5x4 entera y determinar cuántos múltiplos de 5 hay almacenados en ella.
matriz = []
contador = 0
for i in range(5):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Elige un número: ")))
for i in range(5):
    for j in range(4):
        if int(matriz[i][j] % 5) == 0:
            contador = contador + 1
print("Cantidad de números múltiplos de 5: " + str(contador))

#18. Leer una matriz 5x5 entera y determinar en qué posición exacta se encuentra el mayor múltiplo
# de 8.
matriz = []
mayor = 0
multiplos8 = []
columna = 0
fila = 0
for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(int(input("Elige números para la primera matriz: ")))
for i in range(5):
    for j in range(5):
        if matriz[i][j] % 8 == 0:
            multiplos8.append(matriz[i][j])
mayor = multiplos8[0]        
for multiplo in multiplos8:
    if multiplo > mayor:
        mayor = multiplo
for i in range(5):
    fila = fila + 1
    columna = 0
    for j in range(5):
        columna = columna + 1
        if matriz[i][j] == mayor:
            print("Posicion del mayor multiplo de ocho: Fila: " + str(fila) + ". Columna: " + str(columna) + ".")
            break

#19. Leer dos matrices 4x5 entera y determinar si sus contenidos son exactamente iguales.
matriz1 = []
matriz2 = []
contador = 0
for i in range(4):
    matriz1.append([])
    for j in range(5):
        matriz1[i].append(int(input("Elige un número para la primera matriz: ")))
for i in range(4):
    matriz2.append([])
    for j in range(5):
        matriz2[i].append(int(input("Elige un número para la segunda matriz: ")))
for i in range(4):
    for j in range(5):
        if matriz1[i][j] == matriz2[i][j]:
            contador = contador + 1
if contador == 20:
    print("Las dos matrices son exactamente iguales.")
else:
    print("Las dos matrices no son exactamente iguales.")

#20. Leer dos matrices 4x5 entera, luego leer un entero y determinar si cada uno de los elementos
# de una de las matrices es igual a cada uno de los elementos de la otra matriz multiplicado por
# el entero leído.
matriz1 = []
matriz2 = []
num = 0
contador = 0
for i in range(4):
    matriz1.append([])
    for j in range(5):
        matriz1[i].append(int(input("Elige un número para la primera matriz: ")))
for i in range(4):
    matriz2.append([])
    for j in range(5):
        matriz2[i].append(int(input("Elige un número para la segunda matriz: ")))
num = int(input("Elige un número para multiplicar por la matriz: "))
for i in range(4):
    for j in range(5):
        if matriz1[i][j] == matriz2[i][j] * num:
            contador = contador + 1
if contador == 20:
    print("Los datos de la primera matriz son el resultado de los datos de la segunda matriz multiplicados por el número elegido.")
else:
    print("Los datos de la primera matriz no son el resultado de los datos de la segunda matriz multiplicados por el número elegido.")
contador = 0
for i in range(4):
    for j in range(5):
        if matriz2[i][j] == matriz1[i][j] * num:
            contador = contador + 1
if contador == 20:
    print("Los datos de la segunda matriz son el resultado de los datos de la primera matriz multiplicados por el número elegido.")
else:
    print("Los datos de la segunda matriz no son el resultado de los datos de la primera matriz multiplicados por el número elegido.")
