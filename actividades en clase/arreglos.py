#1 problema calcular el producto todos los numeros enteros + de 1 hasta n ENTRADA/SALIDA: n = 5 devuelve 120
#reto asegurarse de validar  que ocurre en la primera caja si entra un numero negativo para evitar desvordamiento de pila 
# pasos la firma del metodo crea un metodo publico que reciba un numero entero int o long y  reciba un parametro n 
# seguridad si n es menor a 0 lanza una excepcion de tipo ValueError que proteja la memoria
# el caso base si n es igual a 0 o 1 devuelve 1 sirectamente (freno de mano)
# recursividad multiplica n por el resultado de llamar al metodo con n-1 y devuelve el resultado


def producto(n):
    if n < 0:
        raise ValueError("El numero debe ser mayor o igual a 0.")

    print(f"Entrando a producto({n})")

    if n == 0 or n == 1:
        print(f"Caso base: producto({n}) = 1")
        return 1

    resultado = n * producto(n - 1)

    print(f"Regresando: {n} * producto({n - 1}) = {resultado}")

    return resultado


n = 5
resultado = producto(n)

print(f"\nResultado final: {resultado}")

