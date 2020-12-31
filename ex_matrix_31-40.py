
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
