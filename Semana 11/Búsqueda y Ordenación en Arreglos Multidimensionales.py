def bubble_sort(row):
    n = len(row)
    for i in range(n):
        for j in range(0, n-i-1):
            if row[j] > row[j+1]:
                row[j], row[j+1] = row[j+1], row[j]
    return row

def find_number(matriz, numero):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                return i, j
    return None

# Aquí cambias los numeros de la matriz y le pones los que tu quieras
matriz = [
    [91, 43, 55],
    [63, 81, 11],
    [37, 52, 76]
]

print("Matriz desordenada:")
for row in matriz:
    print(row)

#Aquí debes cambiar el numéro segun la fila que quieras ordenar, ya sea 0, 1 o 2
row_index = 0
matriz[row_index] = bubble_sort(matriz[row_index])

print("\nMatriz con la fila ordenada:")
for row in matriz:
    print(row)

numerobuscado = int(input("\nIngrese el número que desea buscar: "))
posicion = find_number(matriz, numerobuscado)

if posicion:
    print(f"\nEl número {numerobuscado} se encuentra en la fila {posicion[0]} y columna {posicion[1]}.")
else:
    print(f"\nEl número {numerobuscado} no se encuentra en la matriz.")
