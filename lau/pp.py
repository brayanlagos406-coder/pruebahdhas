A = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]

B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def sumar_matrices(A, B):

    filas_A = 0
    filas_B = 0

    for fila in A:
        filas_A = filas_A + 1

    for fila in B:
        filas_B = filas_B + 1

    if filas_A != filas_B:
        return None

    columnas_A = 0
    columnas_B = 0

    for elemento in A[0]:
        columnas_A = columnas_A + 1

    for elemento in B[0]:
        columnas_B = columnas_B + 1

    if columnas_A != columnas_B:
        return None

    resultado = []

    for i in range(filas_A):

        fila = []

        for j in range(columnas_A):
            fila.append(A[i][j] + B[i][j])

        resultado.append(fila)

    return resultado


def restar_matrices(A, B):

    filas_A = 0
    filas_B = 0

    for fila in A:
        filas_A = filas_A + 1

    for fila in B:
        filas_B = filas_B + 1

    if filas_A != filas_B:
        return None

    columnas_A = 0
    columnas_B = 0

    for elemento in A[0]:
        columnas_A = columnas_A + 1

    for elemento in B[0]:
        columnas_B = columnas_B + 1

    if columnas_A != columnas_B:
        return None

    resultado = []

    for i in range(filas_A):

        fila = []

        for j in range(columnas_A):
            fila.append(A[i][j] - B[i][j])

        resultado.append(fila)

    return resultado


def multiplicar_escalar(A, numero):

    resultado = []

    for i in range(3):

        fila = []

        for j in range(3):
            fila.append(A[i][j] * numero)

        resultado.append(fila)

    return resultado


def transpuesta(A):

    resultado = []

    for j in range(3):

        fila = []

        for i in range(3):
            fila.append(A[i][j])

        resultado.append(fila)

    return resultado


def mostrar_matriz(matriz):

    for fila in matriz:
        print(fila)


print("SUMA DE A + B")
mostrar_matriz(sumar_matrices(A, B))

print("\nRESTA DE A - B")
mostrar_matriz(restar_matrices(A, B))

print("\nA MULTIPLICADA POR 2")
mostrar_matriz(multiplicar_escalar(A, 2))

print("\nTRANSPUESTA DE A")
mostrar_matriz(transpuesta(A))