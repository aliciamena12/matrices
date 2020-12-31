
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

#21. Leer dos matrices 4x5 enteras y determinar cuántos datos tienen en común.
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
print("Datos que tienen en común las dos matrices: " + str(contador))

#22. Leer dos matrices 4x5 enteras y determinar si el número mayor almacenado en la primera está
# en la segunda.
matriz1 = []
matriz2 = []
mayor1 = 0
for i in range(4):
    matriz1.append([])
    for j in range(5):
        matriz1[i].append(int(input("Elige números para la primera matriz: ")))
for i in range(4):
    matriz2.append([])
    for j in range(5):
        matriz2[i].append(int(input("Elige números para la segunda matriz: ")))
for i in range(4):
    for j in range(5):
        if matriz1[i][j] > mayor1:
            mayor1 = matriz1[i][j]
for i in range(4):
    for j in range(5):
        if matriz2[i][j] == mayor1:
            esta = True
            break
        esta = False
if esta == True:
    print("El número mayor de la primera matriz está almacenado en la segunda matriz.")
if esta == False:
    print("El número mayor de la primera matriz no está almacenado en la segunda matriz.")

#23. Leer dos matrices 4x5 enteras y determinar si el número mayor de una de las matrices es igual
# al número mayor de la otra matriz.
matriz1 = []
matriz2 = []
mayor1 = 0
mayor2 = 0
for i in range(4):
    matriz1.append([])
    for j in range(5):
        matriz1[i].append(int(input("Elige números para la primera matriz: ")))
for i in range(4):
    matriz2.append([])
    for j in range(5):
        matriz2[i].append(int(input("Elige números para la segunda matriz: ")))
for i in range(4):
    for j in range(5):
        if matriz1[i][j] > mayor1:
            mayor1 = matriz1[i][j]
for i in range(4):
    for j in range(5):
        if matriz2[i][j] > mayor2:
            mayor2 = matriz2[i][j]
if mayor1 == mayor2:
    print("El número mayor de la primera matriz coincide con el mayor número de la segunda matriz.")
else:
    print("El número mayor de la primera matriz no coincide con el mayor número de la segunda matriz.")

#24. Leer dos matrices 4x5 enteras y determinar si el mayor número primo de una de las matrices
# también se encuentra en la otra matriz.
matriz1 = []
matriz2 = []
primos1 = []
primos2 = []
mayor1 = 0
mayor2 = 0
is_prime = False
esta = False
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
        for x in range(2, (matriz1[i][j] - 1)):
            if int(matriz1[i][j] % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or matriz1[i][j] == 2 or matriz1[i][j] == 3:
            primos1.append(matriz1[i][j])
for i in range(4):
    for j in range(5):
        for x in range(2, (matriz2[i][j] - 1)):
            if int(matriz2[i][j] % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or matriz2[i][j] == 2 or matriz2[i][j] == 3:
            primos2.append(matriz2[i][j])          
mayor1 = primos1[0]
for primo1 in primos1:
    if primo1 > mayor1:
        mayor1 = primo1
mayor2 = primos2[0]
for primo2 in primos2:
    if primo2 > mayor2:
        mayor2 = primo2

for i in range(4):
    for j in range(5):
        if matriz1[i][j] == mayor2:
            print("El mayor número primo de la segunda matriz esta en la primera matriz.")
            esta = True
            break
if esta != True:
    print("El mayor número primo de la segunda matriz no esta en la primera matriz.")
for i in range(4):
    for j in range(5):
        if matriz2[i][j] == mayor1:
            print("El mayor número primo de la primera matriz esta en la segunda matriz.")
            esta = True
            break
if esta != True:
    print("El mayor número primo de la primera matriz no esta en la segunda matriz.")
if mayor1 == mayor2:
    print("Las dos matrices tienen el mismo mayor número primo.")

#25. Leer dos matrices 4x5 enteras y determinar si el mayor número primo de una de las matrices
# es también el mayor número primo de la otra matriz.
matriz1 = []
matriz2 = []
primos1 = []
primos2 = []
mayor1 = 0
mayor2 = 0
contador2 = 0
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
        for x in range(2, (matriz1[i][j] - 1)):
            if int(matriz1[i][j] % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or matriz1[i][j] == 2 or matriz1[i][j] == 3:
            primos1.append(matriz1[i][j])
for i in range(4):
    for j in range(5):
        for x in range(2, (matriz2[i][j] - 1)):
            if int(matriz2[i][j] % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or matriz2[i][j] == 2 or matriz2[i][j] == 3:
            primos2.append(matriz2[i][j])          
mayor1 = primos1[0]
for primo1 in primos1:
    if primo1 > mayor1:
        mayor1 = primo1
mayor2 = primos2[0]
for primo2 in primos2:
    if primo2 > mayor2:
        mayor2 = primo2
if mayor1 == mayor2:
    print("Las dos matrices tienen el mismo mayor número primo.")
else:
    print("Las dos matrices no tienen el mismo mayor número primo.")

#26. Leer dos matrices 4x5 enteras y determinar si la cantidad de números pares almacenados en
# una matriz es igual a la cantidad de números pares almacenados en la otra matriz.
matriz1 = []
matriz2 = []
contador1 = 0
contador2 = 0
for i in range(5):
    matriz1.append([])
    for j in range(5):
        matriz1[i].append(int(input("Elige un número para la primera matriz: ")))
for i in range(5):
    matriz2.append([])
    for j in range(5):
        matriz2[i].append(int(input("Elige un número para la segunda matriz: ")))
for i in range(5):
    for j in range(5):
        if matriz1[i][j] % 2 == 0:
            contador1 = contador1 + 1
for i in range(5):
    for j in range(5):
        if matriz2[i][j] % 2 == 0:
            contador2 = contador2 + 1            
if contador1 == contador2:
    print("Las dos matrices tienen la misma cantidad de números pares.")
else:
    print("Las dos matrices no tienen la misma cantidad de números pares.")

#27. Leer dos matrices 4x5 enteras y determinar si la cantidad de números primos almacenados en
# una matriz es igual a la cantidad de números primos almacenados en la otra matriz.
matriz1 = []
matriz2 = []
contador1 = 0
contador2 = 0
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
        for x in range(2, (matriz1[i][j] - 1)):
            if int(matriz1[i][j] % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or matriz1[i][j] == 2 or matriz1[i][j] == 3:
            contador1 = contador1 + 1
for i in range(4):
    for j in range(5):
        for x in range(2, (matriz2[i][j] - 1)):
            if int(matriz2[i][j] % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or matriz2[i][j] == 2 or matriz2[i][j] == 3:
            contador2 = contador2 + 1            
     
if contador1 == contador2:
    print("Las dos matrices tienen la misma cantidad de números primos.")
else:
    print("Las dos matrices no tienen la misma cantidad de números primos.")

#28. Leer una matriz 4x6 entera y determinar en qué posiciones se encuentran los números cuyo
# penúltimo dígito sea el 5.
matriz = []
penultimo_cinco = []
fila = 0
columna = 0
for i in range(4):
    matriz.append([])
    for j in range(6):
        matriz[i].append(int(input("Elige números para la matriz: ")))
for i in range(4):
    for j in range(6):
        if (int(matriz[i][j] / 10)) % 10 == 5:
            penultimo_cinco.append(matriz[i][j])
print("Posiciones de los números que tienen 5 como penúltimo dígito: ")
for number in penultimo_cinco:
    fila = 0
    for i in range(4):
        fila = fila + 1
        columna = 0
        for j in range(6):
            columna = columna + 1
            if matriz[i][j] == number:
                print("Fila: " + str(fila) + ". Columna: " + str(columna) + ".")

#29. Leer una matriz 4x6 entera y determinar si alguno de sus números está repetido al menos 3
# veces.
matriz = []
contador = 0
repeticiones = []
for i in range(4):
    matriz.append([])
    for j in range(6):
        matriz[i].append(int(input("Elige números para la matriz: ")))
for i in range(4):
    for j in range(6):
        contador = 0
        for x in range(4):
            for y in range(6):
                if matriz[i][j] == matriz[x][y]:
                    contador = contador + 1
        repeticiones.append(contador)
for num in repeticiones:
    if num >= 3:
        print("Al menos uno de los números de la matriz está repetido al menos 3 veces.")
        break
    else:
        print("Ninguno de los números de la matriz está repetido al menos 3 veces.")
        break

#30. Leer una matriz 4x6 entera y determinar cuántas veces está en ella el número menor.
matriz = []
mayor = 0
contador = 0
for i in range(4):
    matriz.append([])
    for j in range(6):
        matriz[i].append(int(input("Elige un número: ")))
menor = matriz[0][0]
for i in range(4):
    for j in range(6):
        if matriz[i][j] < menor:
            menor = matriz[i][j]
for i in range(4):
    for j in range(6):
        if matriz[i][j] == menor:
            contador = contador + 1
print("Cantidad de veces que se repite el número menor: " + str(contador))

#31. Leer una matriz 4x6 entera y determinar en qué posiciones están los menores por fila.
matriz = []
menor = 0
menores = []
posiciones = []
for i in range(4):
    matriz.append([])
    for j in range(6):
        matriz[i].append(int(input("Elige números para la matriz: ")))
for i in range(4):
    menor = matriz[i][0] 
    posicion = "Fila = " + str(i + 1) + ", Columna = " + str(1)
    for j in range(6):
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            posicion = "Fila = " + str(i + 1) + ", Columna = " + str(j + 1)
    posiciones.append(posicion)
    menores.append(menor)

print("Posiciones de los menores números por fila: ")
for i in range(4):
    print(str(menores[i]) + " => " + str(posiciones[i])) 

#32. Leer una matriz 4x6 entera y determinar en qué posiciones están los menores primos por fila.
matriz = []
menor = 0
mayor = 0
menores = []
posicion = ""
posiciones = []
contador = 0
for i in range(4):
    matriz.append([])
    for j in range(6):
        matriz[i].append(int(input("Elige un número para la matriz: ")))
mayor = matriz[0][0]
for i in range(4):
    for j in range(6):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j] + 1
for i in range(4):
    for j in range(6):
        for x in range(2, (matriz[i][j] - 1)):
            if int(matriz[i][j] % x) == 0:        
                matriz[i][j] = mayor
for i in range(4):
    posicion = "Fila = " + str(i + 1) + ", Columna = " + str(1)
    menor = matriz[i][0]
    for j in range(6):
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            posicion = "Fila = " + str(i + 1) + ", Columna = " + str(j + 1)
    posiciones.append(posicion)
    menores.append(menor)
print("Posiciones de los menores números primos por fila: ")
for i in range(4):
    if menores[i] == mayor:
        print("En la fila " + str(i + 1) + " no hay números primos.")
    else:
        print(str(menores[i]) + " => " + str(posiciones[i])) 

#33. Leer una matriz 4x6 entera y determinar en qué posiciones están los menores pares por fila.
matriz = []
menor = 0
mayor = 0
menores = []
posicion = ""
posiciones = []
contador = 0
for i in range(4):
    matriz.append([])
    for j in range(6):
        matriz[i].append(int(input("Elige un número para la matriz: ")))
print(matriz)
mayor = matriz[0][0]
for i in range(4):
    for j in range(6):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j] + 1
for i in range(4):
    for j in range(6):
        if matriz[i][j] % 2 != 0:
                matriz[i][j] = mayor
for i in range(4):
    posicion = "Fila = " + str(i + 1) + ", Columna = " + str(1)
    menor = matriz[i][0]
    for j in range(6):
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            posicion = "Fila = " + str(i + 1) + ", Columna = " + str(j + 1)
    posiciones.append(posicion)
    menores.append(menor)
print("Posiciones de los menores números pares por fila: ")
for i in range(4):
    if menores[i] == mayor:
        print("En la fila " + str(i + 1) + " no hay números pares.")
    else:
        print(str(menores[i]) + " => " + str(posiciones[i])) 

#34. Leer una matriz 4x6 entera y determinar cuántos de los números almacenados en ella
# pertenecen a los 100 primeros elementos de la serie de Fibonacci.
fibonacci = []
matriz = []
contador = 0
x = 0
y = 1
for number in range(0, 50):
    fibonacci.append(x)
    fibonacci.append(y)
    x = x + y
    y = x + y

for i in range(4):
    matriz.append([])
    for j in range(6):
        matriz[i].append(int(input("Elige números para la matriz: ")))
print(matriz)
for i in range(4):
    for j in range(6):
        for dato in fibonacci:
            if matriz[i][j] == dato:
                contador = contador + 1
print("Cantidad de números que aparecen en los 100 primeros numeros de la lista de Fibonacci son: " + str(contador))

#35. Leer dos matrices 4x6 enteras y determinar cuál es el mayor dato almacenado en ellas que
# pertenezca a la Serie de Fibonacci.
matriz1 = []
matriz2 = []
mayor = 0
fibonacci = []
matriz1fibo = []
matriz2fibo = []
x = 0
y = 1
mayorfibo1 = 0
mayorfibo2 = 0
for i in range(4):
    matriz1.append([])
    for j in range(6):
        matriz1[i].append(int(input("Elige un número para la primera matriz: ")))
for i in range(4):
    matriz2.append([])
    for j in range(6):
        matriz2[i].append(int(input("Elige un número para la segunda matriz: ")))
for i in range(4):
    for j in range(6):
        if matriz1[i][j] > mayor:
            mayor = matriz1[i][j]
for i in range(4):
    for j in range(6):
        if matriz2[i][j] > mayor:
            mayor = matriz2[i][j]
for number in range(0, (int(mayor / 10))):
    fibonacci.append(x)
    fibonacci.append(y)
    x = x + y
    y = x + y
for dato in fibonacci:
    for i in range(4):
        for j in range(6):
            if matriz1[i][j] == dato:
                matriz1fibo.append(matriz1[i][j])
for dato in fibonacci:
    for i in range(4):
        for j in range(6):
            if matriz2[i][j] == dato:
                matriz2fibo.append(matriz2[i][j])
for num in matriz1fibo:
    if num > mayorfibo1:
        mayorfibo1 = num
print("El mayor número de la primera matriz que pertenece a la serie de Fibonacci es: " + str(mayorfibo1))
for num in matriz2fibo:
    if num > mayorfibo2:
        mayorfibo2 = num
print("El mayor número de la segunda matriz que pertenece a la serie de Fibonacci es: " + str(mayorfibo2))

#36. Leer dos matrices 4x6 enteras y determinar si el mayor número almacenado en una de ellas
# # que pertenezca a la Serie de Fibonacci es igual al mayor número almacenado en la otra matriz
# que pertenezca a la Serie de Fibonacci.
matriz1 = []
matriz2 = []
mayor = 0
fibonacci = []
matriz1fibo = []
matriz2fibo = []
x = 0
y = 1
mayorfibo1 = 0
mayorfibo2 = 0
for i in range(4):
    matriz1.append([])
    for j in range(6):
        matriz1[i].append(int(input("Elige un número para la primera matriz: ")))
for i in range(4):
    matriz2.append([])
    for j in range(6):
        matriz2[i].append(int(input("Elige un número para la segunda matriz: ")))
for i in range(4):
    for j in range(6):
        if matriz1[i][j] > mayor:
            mayor = matriz1[i][j]
for i in range(4):
    for j in range(6):
        if matriz2[i][j] > mayor:
            mayor = matriz2[i][j]
for number in range(0, (int(mayor / 10))):
    fibonacci.append(x)
    fibonacci.append(y)
    x = x + y
    y = x + y
for dato in fibonacci:
    for i in range(4):
        for j in range(6):
            if matriz1[i][j] == dato:
                matriz1fibo.append(matriz1[i][j])
for dato in fibonacci:
    for i in range(4):
        for j in range(6):
            if matriz2[i][j] == dato:
                matriz2fibo.append(matriz2[i][j])
for num in matriz1fibo:
    if num > mayorfibo1:
        mayorfibo1 = num
for num in matriz2fibo:
    if num > mayorfibo2:
        mayorfibo2 = num
if mayorfibo1 == mayorfibo2:
    print("Las dos matrices coinciden en el mismo mayor número que pertenece a la serie de Fibonacci.")
else:
    print("Las dos matrices no coinciden en el mismo mayor número que pertenece a la serie de Fibonacci.")

#37. Leer dos matrices 4x6 enteras y determinar si el número mayor de una matriz se encuentra en
# la misma posición exacta en la otra matriz.
matriz1 = []
matriz2 = []
mayor1 = 0
mayor2 = 0
fila1 = 0
columna1 = 0
fila2 = 0
columna2 = 0
for i in range(4):
    matriz1.append([])
    for j in range(6):
        matriz1[i].append(int(input("Elige un número para la primera matriz: ")))
for i in range(4):
    matriz2.append([])
    for j in range(6):
        matriz2[i].append(int(input("Elige un número para la segunda matriz: ")))
for i in range(4):
    for j in range(6):
        if matriz1[i][j] > mayor1:
            mayor1 = matriz1[i][j]
            fila1 = i
            columna1 = j
for i in range(4):
    for j in range(6):
        if matriz2[i][j] > mayor2:
            mayor2 = matriz2[i][j]
            fila2 = i
            columna2 = j
if matriz2[fila1][columna1] == mayor1:
    print("El número más grande de la primera matriz se encuentra en la misma posición en la segunda matriz.")
else:
    print("El número más grande de la primera matriz no se encuentra en la misma posición en la segunda matriz.")
if matriz1[fila2][columna2] == mayor2:
    print("El número más grande de la segunda matriz se encuentra en la misma posición en la primera matriz.")
else:
    print("El número más grande de la segunda matriz no se encuentra en la misma posición en la primera matriz.")
   
#38. Leer dos matrices 4x6 enteras y determinar si el mayor número primo de una matriz está
# repetido en la otra matriz.
matriz1 = []
matriz2 = []
primos1 = []
primos2 = []
mayor1 = 0
mayor2 = 0
is_prime = False
esta = False
for i in range(4):
    matriz1.append([])
    for j in range(6):
        matriz1[i].append(int(input("Elige un número para la primera matriz: ")))
for i in range(4):
    matriz2.append([])
    for j in range(6):
        matriz2[i].append(int(input("Elige un número para la segunda matriz: ")))
for i in range(4):
    for j in range(6):
        for x in range(2, (matriz1[i][j] - 1)):
            if int(matriz1[i][j] % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or matriz1[i][j] == 2 or matriz1[i][j] == 3:
            primos1.append(matriz1[i][j])
for i in range(4):
    for j in range(6):
        for x in range(2, (matriz2[i][j] - 1)):
            if int(matriz2[i][j] % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or matriz2[i][j] == 2 or matriz2[i][j] == 3:
            primos2.append(matriz2[i][j])          
mayor1 = primos1[0]
for primo1 in primos1:
    if primo1 > mayor1:
        mayor1 = primo1
mayor2 = primos2[0]
for primo2 in primos2:
    if primo2 > mayor2:
        mayor2 = primo2

for i in range(4):
    for j in range(6):
        if matriz1[i][j] == mayor2:
            print("El mayor número primo de la segunda matriz esta en la primera matriz.")
            esta = True
            break
if esta != True:
    print("El mayor número primo de la segunda matriz no esta en la primera matriz.")
for i in range(4):
    for j in range(6):
        if matriz2[i][j] == mayor1:
            print("El mayor número primo de la primera matriz esta en la segunda matriz.")
            esta = True
            break
if esta != True:
    print("El mayor número primo de la primera matriz no esta en la segunda matriz.")
if mayor1 == mayor2:
    print("Las dos matrices tienen el mismo mayor número primo.")

#39. Leer dos matrices 4x6 enteras y determinar si el promedio de las “esquinas” de una matriz es
# igual al promedio de las “esquinas” de la otra matriz.
matriz1 = []
matriz2 = []
promedio1 = 0
promedio2 = 0
for i in range(4):
    matriz1.append([])
    for j in range(6):
        matriz1[i].append(int(input("Elige números para la primera matriz: ")))
for i in range(4):
    matriz2.append([])
    for j in range(6):
        matriz2[i].append(int(input("Elige números para la segunda matriz: ")))
promedio1 = int((matriz1[0][0] + matriz1[0][5] + matriz1[3][0] + matriz1[3][5]) / 4)
promedio2 = int((matriz2[0][0] + matriz2[0][5] + matriz2[3][0] + matriz2[3][5]) / 4)
if promedio1 == promedio2:
    print("El promedio de las esquinas de las dos matrices es el mismo.")
else:
    print("El promedio de las esquinas de las dos matrices no es el mismo.")

#40. Leer dos matrices 5x5 enteras y determinar si el promedio entero de los elementos de la
# diagonal de una matriz es igual al promedio de los elementos de la diagonal de la otra matriz.
matriz1 = []
matriz2 = []
suma1 = 0
suma2 = 0
promedio1 = 0
promedio2 = 0
for i in range(5):
    matriz1.append([])
    for j in range(5):
        matriz1[i].append(int(input("Elige números para la primera matriz: ")))
for i in range(5):
    matriz2.append([])
    for j in range(5):
        matriz2[i].append(int(input("Elige números para la segunda matriz: ")))
for i in range(5):
    for j in range(5):
            if i == j:
                suma1 = suma1 + matriz1[i][j]
promedio1 = int(suma1 / 5)
for i in range(5):
    for j in range(5):
            if i == j:
                suma2 = suma2 + matriz2[i][j]
promedio2 = int(suma2 / 5)
if promedio1 == promedio2:
    print("El promedio de los números de la diagonal de la segunda matriz es igual al promedio de la diagonal de la segunda matriz.")
else:
    print("El promedio de los números de la diagonal de la segunda matriz no es igual al promedio de la diagonal de la segunda matriz.")

#41. Leer dos matrices 5x5 enteras y determinar si el promedio entero de todos los elementos que
# no están en la diagonal de una matriz es igual al promedio entero de todos los elementos que
# no están en la diagonal de la otra matriz.
matriz1 = []
matriz2 = []
contador1 = 0
contador2 = 0
suma1 = 0
suma2 = 0
promedio1 = 0
promedio2 = 0
for i in range(5):
    matriz1.append([])
    for j in range(5):
        matriz1[i].append(int(input("Elige números para la primera matriz: ")))
for i in range(5):
    matriz2.append([])
    for j in range(5):
        matriz2[i].append(int(input("Elige números para la segunda matriz: ")))
for i in range(5):
    for j in range(5):
            if i != j:
                contador1 = contador1 + 1
                suma1 = suma1 + matriz1[i][j]
promedio1 = int(suma1 / contador1)
for i in range(5):
    for j in range(5):
            if i != j:
                contador2 = contador2 + 2
                suma2 = suma2 + matriz2[i][j]
promedio2 = int(suma2 / contador2)

if promedio1 == promedio2:
    print("El promedio de los números que no estan en la diagonal de la primera matriz es igual al promedio de los que no estan en la diagonal de la segunda matriz.")
else:
    print("El promedio de los números que no estan en la diagonal de la primera matriz no es igual al promedio de los que no estan en la diagonal de la segunda matriz.")

#42. Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números primos de
# una matriz se encuentra almacenado en la otra matriz.
matriz1 = []
matriz2 = []
primos1 = []
primos2 = []
contador1 = 0
contador2 = 0
suma1 = 0
suma2 = 0
promedio1 = 0
promedio2 = 0
is_prime = False
esta = False
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
        for x in range(2, (matriz1[i][j] - 1)):
            if int(matriz1[i][j] % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or matriz1[i][j] == 2 or matriz1[i][j] == 3:
            contador1 = contador1 + 1
            primos1.append(matriz1[i][j])
for i in range(4):
    for j in range(5):
        for x in range(2, (matriz2[i][j] - 1)):
            if int(matriz2[i][j] % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True or matriz2[i][j] == 2 or matriz2[i][j] == 3:
            contador2 = contador2 + 1
            primos2.append(matriz2[i][j])          
for primo1 in primos1:
    suma1 = suma1 + primo1
promedio1 = int(suma1 / contador1)
for primo2 in primos2:
    suma2 = suma2 + primo2
promedio2 = int(suma2 / contador2)

for i in range(4):
    for j in range(5):
        if matriz1[i][j] == promedio2:
            print("El promedio de los números primos de la segunda matriz esta en la primera matriz.")
            esta = True
            break
if esta != True:
    print("El promedio de los números primos de la segunda matriz no esta en la primera matriz.")
for i in range(4):
    for j in range(5):
        if matriz2[i][j] == promedio1:
            print("El promedio de los números primos de la primera matriz esta en la segunda matriz.")
            esta = True
            break
if esta != True:
    print("El promedio de los números primos de la primera matriz no esta en la segunda matriz.")

#43. Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números pares de una
# matriz es igual al promedio de los números pares de la otra matriz.
matriz1 = []
matriz2 = []
pares1 = []
pares2 = []
suma1 = 0
suma2 = 0
contador1 = 0
contador2 = 0
promedio1 = 0
promedio2 = 0
for i in range(5):
    matriz1.append([])
    for j in range(5):
        matriz1[i].append(int(input("Elige un número para la primera matriz: ")))
for i in range(5):
    matriz2.append([])
    for j in range(5):
        matriz2[i].append(int(input("Elige un número para la segunda matriz: ")))
for i in range(5):
    for j in range(5):
        if int(matriz1[i][j] % 2) == 0:
            contador1 = contador1 + 1
            pares1.append(matriz1[i][j])
for i in range(5):
    for j in range(5):
        if int(matriz2[i][j] % 2) == 0:
            contador2 = contador2 + 1
            pares2.append(matriz2[i][j])
for par1 in pares1:
    suma1 = suma1 + par1
promedio1 = int(suma1 / contador1)
for par2 in pares2:
    suma2 = suma2 + par2
promedio2 = int(suma2 / contador2)
if promedio1 == promedio2:
    print("El promedio entero de los números pares de cada matriz es el mismo.")
else:
    print("El promedio entero de los números pares de cada matriz no es el mismo.")

#44. Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números terminados
# en 4 de una matriz se encuentra al menos 3 veces en la otra matriz.
matriz1 = []
matriz2 = []
cuatros1 = []
cuatros2 = []
suma1 = 0
suma2 = 0
promedio1 = 0
promedio2 = 0
contador1 = 0
contador2 = 0
cantidad1 = 0
cantidad2 = 0
for i in range(5):
    matriz1.append([])
    for j in range(5):
        matriz1[i].append(int(input("Elige números para la primera matriz: ")))
for i in range(5):
    matriz2.append([])
    for j in range(5):
        matriz2[i].append(int(input("Elige números para la segunda matriz: ")))
for i in range(5):
    for j in range(5):
        if matriz1[i][j] % 10 == 4:
            contador1 = contador1 + 1
            cuatros1.append(matriz1[i][j])
for i in range(5):
    for j in range(5):
        if matriz2[i][j] % 10 == 4:
            contador2 = contador2 + 1
            cuatros2.append(matriz2[i][j])
for cuatro1 in cuatros1:
    suma1 = suma1 + cuatro1
promedio1 = int(suma1 / contador1)
for cuatro2 in cuatros2:
    suma2 = suma2 + cuatro2
promedio2 = int(suma2 / contador2)
for i in range(5):
    for j in range(5):
        if matriz1[i][j] == promedio2:
            cantidad1 = cantidad1 + 1
for i in range(5):
    for j in range(5):
        if matriz2[i][j] == promedio1:
            cantidad2 = cantidad2 + 1
if cantidad1 >= 3:
    print("El promedio de los números acabados en 4 de la segunda matriz esta al menos 3 veces repetido en la primera matriz.")
else:
    print("El promedio de los números acabados en 4 de la segunda matriz no llega a estar 3 veces repetido en la primera matriz.")
if cantidad2 >= 3:
    print("El promedio de los números acabados en 4 de la primera matriz esta al menos 3 veces repetido en la segunda matriz.")
else:
    print("El promedio de los números acabados en 4 de la primera matriz no llega a estar 3 veces repetido en la segunda matriz.")

#45. Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números mayores de
# cada fila de una matriz es igual al promedio de los números mayores de cada fila de la otra
# matriz.
matriz1 = []
matriz2 = []
mayor = 0
mayores1 = []
mayores2 = []
suma1 = 0
suma2 = 0
promedio1 = 0
promedio2 = 0
for i in range(5):
    matriz1.append([])
    for j in range(5):
        matriz1[i].append(int(input("Elige números para la primera matriz: ")))
for i in range(5):
    matriz2.append([])
    for j in range(5):
        matriz2[i].append(int(input("Elige números para la segunda matriz: ")))
for i in range(5):
    mayor = matriz1[i][0] 
    for j in range(5):
        if matriz1[i][j] > mayor:
            mayor = matriz1[i][j]
    mayores1.append(mayor)
for i in range(5):
    mayor = matriz2[i][0] 
    for j in range(5):
        if matriz2[i][j] > mayor:
            mayor = matriz2[i][j]
    mayores2.append(mayor)
for mayor1 in mayores1:
    suma1 = suma1 + mayor1
promedio1 = int(suma1 / 5)
for mayor2 in mayores2:
    suma2 = suma2 + mayor2
promedio2 = int(suma2 / 5)
if promedio1 == promedio2: 
    print("Los promedios de los números mayores de cada fila de las dos matrices coinciden.")
else:
    print("Los promedios de los números mayores de cada fila de las dos matrices no coinciden.")

#46. Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números menores
# cada fila de una matriz corresponde a alguno de los datos almacenados en las “esquinas” de la
# otra matriz.
matriz1 = []
matriz2 = []
menor = 0
menores1 = []
menores2 = []
suma1 = 0
suma2 = 0
promedio1 = 0
promedio2 = 0
for i in range(5):
    matriz1.append([])
    for j in range(5):
        matriz1[i].append(int(input("Elige números para la primera matriz: ")))
for i in range(5):
    matriz2.append([])
    for j in range(5):
        matriz2[i].append(int(input("Elige números para la segunda matriz: ")))
for i in range(5):
    menor = matriz1[i][0] 
    for j in range(5):
        if matriz1[i][j] < menor:
            menor = matriz1[i][j]
    menores1.append(menor)
for i in range(5):
    menor = matriz2[i][0] 
    for j in range(5):
        if matriz2[i][j] < menor:
            menor = matriz2[i][j]
    menores2.append(menor)
for menor1 in menores1:
    suma1 = suma1 + menor1
promedio1 = int(suma1 / 5)
for menor2 in menores2:
    suma2 = suma2 + menor2
promedio2 = int(suma2 / 5)
if promedio1 == matriz2[0][0] or promedio1 == matriz2[0][4] or promedio1 == matriz2[4][0] or promedio1 == matriz2[4][4]: 
    print("El promedio de los números menores de cada fila de la primera matriz se encuentra en una de las esquinas de la segunda matriz.")
else:
    print("El promedio de los números menores de cada fila de la primera matriz no se encuentra en una de las esquinas de la segunda matriz.")
if promedio2 == matriz1[0][0] or promedio2 == matriz1[0][4] or promedio2 == matriz1[4][0] or promedio2 == matriz1[4][4]: 
    print("El promedio de los números menores de cada fila de la segunda matriz se encuentra en una de las esquinas de la primera matriz.")
else:
    print("El promedio de los números menores de cada fila de la segunda matriz no se encuentra en una de las esquinas de la primera matriz.")

#47. Leer dos matrices 5x5 enteras y determinar si el promedio de los mayores números primos por
# cada fila de una matriz es igual al promedio de los mayores números primos por cada columna
# de la otra matriz.
matriz1 = []
matriz2 = []
mayor = 0
mayores1 = []
mayores2 = []
suma = 0
promedio1 = 0
promedio2 = 0
for i in range(5):
    matriz1.append([])
    for j in range(5):
        matriz1[i].append(int(input("Elige un número para la primera matriz: ")))
for i in range(5):
    matriz2.append([])
    for j in range(5):
        matriz2[i].append(int(input("Elige un número para la segunda matriz: ")))
for i in range(5):
    for j in range(5):
        for x in range(2, (matriz1[i][j] - 1)):
            if int(matriz1[i][j] % x) == 0:
                matriz1[i][j] = 0
                break
for i in range(5):
    for j in range(5):
        for x in range(2, (matriz2[i][j] - 1)):
            if int(matriz2[i][j] % x) == 0:
                matriz2[i][j] = 0
                break
for i in range(5):
    mayor = matriz1[i][0]
    for j in range(5):
        if matriz1[i][j] > mayor:
            mayor = matriz1[i][j]
    mayores1.append(mayor)
for j in range(5):
    mayor = matriz2[0][j]
    for i in range(5):
        if matriz2[i][j] > mayor:
            mayor = matriz2[i][j]
    mayores2.append(mayor)
for num in mayores1:
    suma = suma + num
promedio1 = int(suma / 5)
suma = 0
for num in mayores2:
    suma = suma + num
promedio2 = int(suma / 5)
if promedio1 == promedio2:
    print("El promedio de los mayores números primos de cada fila de la primera matriz coincide con el promedio de los mayores números primos de cada columna de la segunda matriz.")
else:
    print("El promedio de los mayores números primos de cada fila de la primera matriz no coincide con el promedio de los mayores números primos de cada columna de la segunda matriz.")

#48. Leer dos matrices 5x5 entera y determinar si el promedio de los mayores elementos que
# pertenecen a la serie de Fibonacci de cada fila de una matriz es igual al promedio de los
# mayores elementos que pertenecen a la serie de Fibonacci de cada fila de la otra matriz.
matriz1 = []
matriz2 = []
fibonacci = []
x = 0
y = 1
mayor = 0
mayores1 = []
mayores2 = []
suma = 0
promedio1 = 0
promedio2 = 0
for i in range(5):
    matriz1.append([])
    for j in range(5):
        matriz1[i].append(int(input("Elige un número para la primera matriz: ")))
for i in range(5):
    matriz2.append([])
    for j in range(5):
        matriz2[i].append(int(input("Elige un número para la segunda matriz: ")))
for i in range(5):
    for j in range(5):
        if matriz1[i][j] > mayor:
            mayor = matriz1[i][j]
for i in range(5):
    for j in range(5):
        if matriz2[i][j] > mayor:
            mayor = matriz2[i][j]
for number in range(0, int(mayor / 10)):
    fibonacci.append(x)
    fibonacci.append(y)
    x = x + y
    y = x + y
for i in range(5):
    for j in range(5):
        for dato in fibonacci:
            if matriz1[i][j] == dato:
                is_fibo = True
                break
            is_fibo = False
        if is_fibo == False:
            matriz1[i][j] = 0
for i in range(5):
    for j in range(5):
        for dato in fibonacci:           
            if matriz2[i][j] == dato:
                is_fibo = True
                break
            is_fibo = False
        if is_fibo == False:
            matriz2[i][j] = 0
print(matriz1)
print(matriz2)
for i in range(5):
    mayor = matriz1[i][0]
    for j in range(5):
        if matriz1[i][j] > mayor:
            mayor = matriz1[i][j]
    mayores1.append(mayor)
for i in range(5):
    mayor = matriz2[i][0]
    for j in range(5):
        if matriz2[i][j] > mayor:
            mayor = matriz2[i][j]
    mayores2.append(mayor)
for num in mayores1:
    suma = suma + num
promedio1 = int(suma / 5)
suma = 0
for num in mayores2:
    suma = suma + num
promedio2 = int(suma / 5)
if promedio1 == promedio2:
    print("El promedio de los mayores elementos que pertenecen a la serie de Fibonacci de cada fila de las dos matrices coinciden.")
else:
    print("El promedio de los mayores elementos que pertenecen a la serie de Fibonacci de cada fila de las dos matrices no coinciden.")

#49. Leer una matriz 3x3 entera y determinar si el promedio de todos los datos almacenados en ella
# se encuentra también almacenado.
matriz = []
mayor = 0
contador = 0
suma = 0
promedio = 0
for i in range(3):
    matriz.append([])
    for j in range(3):
        matriz[i].append(int(input("Elige un número: ")))
for i in range(3):
    for j in range(3):
        suma = suma + matriz[i][j]
        contador = contador + 1
promedio = int(suma / contador)
print("Promedio de todos los números de la matriz: " + str(promedio))
for i in range(3):
    for j in range(3):
        if matriz[i][j] == promedio:
            print("El promedio de todos los números de la matriz se encuentra tambiíen almacenado.")
            break
        esta = False
    if esta == False:
        print("El promedio de todos los números de la matriz no se encuentra tambiíen almacenado.")

#50. Leer una matriz 5x5 y determinar si el promedio de los elementos que se encuentran en su
# diagonal está almacenado en ella. Mostrar en pantalla en qué posiciones exactas se encuentra
# dicho dato.
matriz = []
suma = 0
promedio = 0
fila = 0
columna = 0
for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(int(input("Elige números para la matriz: ")))
for i in range(5):
    for j in range(5):
            if i == j:
                suma = suma + matriz[i][j]
promedio = int(suma / 5)
for i in range(5):
    for j in range(5):
        if matriz[i][j] == promedio:
            print("El promedio de los números de la diagonal se encuentra en la matriz.")
            esta = True
            break
        esta = False
if esta == False:
    print("El promedio de los números de la diagonal no se encuentra en la matriz.")
if esta == True:
    print("Posiciones en las que se encuentra el promedio de la diagonal: ")
    for i in range(5):
        fila = fila + 1
        columna = 0
        for j in range(5):
            columna = columna + 1
            if matriz[i][j] == promedio:
                print("Fila: " + str(fila) + ". Columna: " + str(columna) + ".")
