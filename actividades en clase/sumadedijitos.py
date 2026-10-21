#suma de dijitos de un numero entero positivo numero entero positivo n ENTRADA/SALIDA: n = 123 devuelve 6 
# reto utilisar  operadores aritmeticos para obtener el resultado sin convertir el numero a cadena de caracteres
# pasos la firma del metodo crea un metodo publico que reciba un numero entero int y recibe un numero a evaluar
# seguridad si el numero es negativo multiplica el numero por -1 para convertirlo en positivo
#caso base si el caso es 0 devuelva 0 
# recursivo suma el dijito menos significativo (n % 10) con el resultado de llamar al metodo con n / 10 y devuelve el resultado
def suma_digitos(n):
    if n < 0:
        n = -n  # Convertir a positivo si es negativo

    print(f"Entrando a suma_digitos({n})")

    if n == 0:
        print(f"Caso base: suma_digitos({n}) = 0")
        return 0

    resultado = (n % 10) + suma_digitos(n // 10)

    print(f"Regresando: ({n} % 10) + suma_digitos({n} // 10) = {resultado}")

    return resultado
n = 1234578
resultado = suma_digitos(n)
