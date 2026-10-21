# Ejercicio 2: Separar números pares e impares

numeros = input("Ingrese una lista de números separados por comas: ").split(",")

pares = []

impares = []

for numero in numeros:

    numero = int(numero)

    if numero % 2 == 0:
        pares.append(numero)

    else:
        impares.append(numero)


print("Lista de números pares:", pares)

print("Lista de números impares:", impares)