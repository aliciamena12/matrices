
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
