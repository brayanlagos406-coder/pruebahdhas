# Nodo de la lista doble.
class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.actual = None

    def insertar_inicio(self, cancion, mostrar=True):
        nuevo = Nodo(cancion)
        if self.cabeza is None:
            self.cabeza = self.cola = self.actual = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        if mostrar:
            print(f"La canción '{cancion}' fue agregada al inicio.")

    def insertar_final(self, cancion):
        nuevo = Nodo(cancion)
        if self.cabeza is None:
            self.cabeza = self.cola = self.actual = nuevo
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo
        print(f"La canción '{cancion}' fue agregada al final.")

    def mostrar_actual(self):
        if self.actual:
            print(f"Canción actual: {self.actual.cancion}")
        else:
            print("No hay canciones en la playlist.")

    def reproducir_actual(self):
        if self.actual:
            print(f"Reproduciendo: {self.actual.cancion}")
        else:
            print("No hay canciones en la playlist.")

    def siguiente_cancion(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            print(f"Reproduciendo: {self.actual.cancion}")
        else:
            print("No hay una canción siguiente.")

    def anterior_cancion(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            print(f"Reproduciendo: {self.actual.cancion}")
        else:
            print("No hay una canción anterior.")

    def mostrar_playlist(self):
        self._mostrar(self.cabeza, "siguiente", "PLAYLIST")

    def mostrar_inversa(self):
        self._mostrar(self.cola, "anterior", "PLAYLIST INVERSA")

    def _mostrar(self, inicio, direccion, titulo):
        if inicio is None:
            print("La playlist está vacía.")
            return
        print(f"\n--- {titulo} ---")
        actual = inicio
        while actual:
            marca = "->" if actual == self.actual else "-"
            estado = "  [REPRODUCIENDO]" if actual == self.actual else ""
            print(f"{marca} {actual.cancion}{estado}")
            actual = getattr(actual, direccion)

    def buscar_cancion(self, cancion):
        actual = self.cabeza
        while actual is not None:
            if actual.cancion.lower() == cancion.lower():
                return True
            actual = actual.siguiente
        return False 

    def insertar_en_posicion(self, cancion, posicion):
        if posicion < 0:
            print("La posición no puede ser negativa.")
            return
        if posicion == 0:
            self.insertar_inicio(cancion, False)
            print(f"La canción '{cancion}' fue insertada en la posición 0.")
            return

        actual = self.cabeza
        for _ in range(posicion - 1):
            if actual is None:
                break
            actual = actual.siguiente
        if actual is None:
            self.insertar_final(cancion)
            return

        nuevo = Nodo(cancion)
        nuevo.siguiente = actual.siguiente
        nuevo.anterior = actual
        if actual.siguiente:
            actual.siguiente.anterior = nuevo
        else:
            self.cola = nuevo
        actual.siguiente = nuevo
        print(f"La canción '{cancion}' fue insertada en la posición {posicion}.")

    def eliminar_cancion(self, cancion):
        actual = self.cabeza
        while actual:
            if actual.cancion.lower() == cancion.lower():
                if self.actual == actual:
                    self.actual = actual.siguiente or actual.anterior
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                print(f"La canción '{cancion}' fue eliminada.")
                return True
            actual = actual.siguiente
        print(f"La canción '{cancion}' no se encuentra en la playlist.")
        return False

    def vaciar_lista(self):
        self.cabeza = self.cola = self.actual = None
        print("La playlist ha sido vaciada.")


playlist = ListaDoble()

# Menú principal.
while True:
    print("\n===================================")
    print("       REPRODUCTOR DE MÚSICA")
    print("===================================")
    print("1. Agregar canción al inicio")
    print("2. Agregar canción al final")
    print("3. Mostrar playlist")
    print("4. Mostrar playlist en orden inverso")
    print("5. Reproducir canción actual")
    print("6. Reproducir siguiente canción")
    print("7. Reproducir canción anterior")
    print("8. Buscar canción")
    print("9. Insertar canción en una posición")
    print("10. Eliminar canción")
    print("11. Vaciar playlist")
    print("12. Salir")
    print("===================================")

    opcion = input("Seleccione una opción: ")
    if opcion in ("1", "2"):
        cancion = input("Ingrese el nombre de la canción: ")
        (playlist.insertar_inicio if opcion == "1" else playlist.insertar_final)(cancion)
    elif opcion == "3":
        playlist.mostrar_playlist()
    elif opcion == "4":
        playlist.mostrar_inversa()
    elif opcion == "5":
        playlist.reproducir_actual()
    elif opcion == "6":
        playlist.siguiente_cancion()
    elif opcion == "7":
        playlist.anterior_cancion()
    elif opcion == "8":
        cancion = input("Ingrese el nombre de la canción a buscar: ")
        resultado = "sí" if playlist.buscar_cancion(cancion) else "no"
        print(f"La canción '{cancion}' {resultado} se encuentra en la playlist.")
        
        
    elif opcion == "9":
        cancion = input("Ingrese el nombre de la canción: ")
        try:
            posicion = int(input("Ingrese la posición donde desea insertar (0 para inicio): "))
            playlist.insertar_en_posicion(cancion, posicion)
        except ValueError:
            print("Debe ingresar un número entero para la posición.")
    elif opcion == "10":
        playlist.eliminar_cancion(input("Ingrese el nombre de la canción a eliminar: "))
    elif opcion == "11":
        playlist.vaciar_lista()
    elif opcion == "12":
        print("Saliendo del reproductor...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")