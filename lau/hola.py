A = [5, 8, 3, 7]
B = [2, 4, 6, 1]


def producto_punto(a, b):

    # Verificar que tengan la misma cantidad de elementos
    if a == [] or b == []:
        return None

    contador_a = 0
    contador_b = 0

    for elemento in a:
        contador_a = contador_a + 1

    for elemento in b:
        contador_b = contador_b + 1

    if contador_a != contador_b:
        return None

    resultado = 0

    for i in range(contador_a):
        resultado = resultado + a[i] * b[i]

    return resultado


def magnitud(vector):

    cantidad = 0
    suma = 0

    for elemento in vector:
        cantidad = cantidad + 1

    for i in range(cantidad):
        suma = suma + vector[i] ** 2

    resultado = suma ** 0.5

    return resultado


producto = producto_punto(A, B)

if producto == None:

    print("Los vectores no tienen la misma longitud.")

else:

    magnitud_A = magnitud(A)
    magnitud_B = magnitud(B)

    coseno = producto / (magnitud_A * magnitud_B)

    print("Producto punto:", producto)
    print("Magnitud de A:", magnitud_A)
    print("Magnitud de B:", magnitud_B)
    print("Coseno del ángulo:", coseno)