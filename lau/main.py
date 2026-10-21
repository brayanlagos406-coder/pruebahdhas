import sys
import lau.operaciones as operaciones


def main():

    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

    print("\n--- OPERACIONES MATEMÁTICAS ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = int(input("Ingrese la operación que desea realizar: "))

    if opcion == 1:
        print("Resultado:", operaciones.sumar(num1, num2))

    elif opcion == 2:
        print("Resultado:", operaciones.restar(num1, num2))

    elif opcion == 3:
        print("Resultado:", operaciones.multiplicar(num1, num2))

    elif opcion == 4:
        if num2 != 0:
            print("Resultado:", operaciones.dividir(num1, num2))
        else:
            print("No se puede dividir entre cero.")

    else:
        print("Opción no válida.")


main()