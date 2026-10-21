# recibe un texto y devulevelo al reves sin ciclos hola devuelve aloh
# reto concatena el primera letra de la cadena al final del resultado de enviar el resto de la palabra a la recursividad 
# la firma devuelve un string  y recibe el texto a invertir
# segiuridad si el texto es vacio devuelve un string vacio
# caso base si el texto es de longitud es 0 o 1 retornalo directamente
# recursividad invoca tu metodo pasandole la subcadena desde la posicion 1 hasta el final y concatenando la primera letra al final del resultado de la llamada recursiva
def invertir_texto(texto):
    if len(texto) == 0:
        return ""

    print(f"Entrando a invertir_texto('{texto}')")

    if len(texto) == 1:
        print(f"Caso base: invertir_texto('{texto}') = '{texto}'")
        return texto

    resultado = invertir_texto(texto[1:]) + texto[0]

    print(f"Regresando: invertir_texto('{texto[1:]}') + '{texto[0]}' = '{resultado}'")

    return resultado

texto = "hola"
resultado = invertir_texto(texto)