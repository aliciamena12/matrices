
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
