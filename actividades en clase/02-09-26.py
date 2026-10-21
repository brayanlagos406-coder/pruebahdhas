class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        


class listacircular:
    def __init__(self):
        self.cabeza = None
        
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = nuevo  # Apunta a sí mismo
        self.cabeza = nuevo
        
        
    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        
        if self.cabeza is None:
            nuevo.siguiente = nuevo  # Apunta a sí mismo
            self.cabeza = nuevo
            return
        actual = self.cabeza # mientras haya nodos, se imprimen uno por uno
        while actual.siguiente != self.cabeza: # Recorre hasta el último nodo
            actual = actual.siguiente # enlaza el último nodo con el nuevo nodo
            
        actual.siguiente = nuevo
        nuevo.siguiente = self.cabeza  # Cierra el círculo
            
        
    def mostrar_lista(self):
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        
        actual = self.cabeza
        while True:
            print(f"[{actual.cancion}]-> ", end="")
            actual = actual.siguiente
            if actual == self.cabeza:  # Si volvemos a la cabeza, terminamos
                break
        print("fin de la lista")
        
    def Buscar(self, cancion):
        if self.cabeza is None:
            print("La lista está vacía.")
            return False
        
        actual = self.cabeza
        while True:
            if actual.cancion == cancion:
                print(f"La canción '{cancion}' fue encontrada en la lista.")
                return True
            actual = actual.siguiente
            if actual == self.cabeza:  # Si volvemos a la cabeza, terminamos
                break
        
        print(f"La canción '{cancion}' no fue encontrada en la lista.")
        return False
        
mi_lista = listacircular()
mi_lista.insertar_inicio("Canción B")
mi_lista.insertar_inicio("Cancion A")
mi_lista.insertar_final("Canción C")
mi_lista.insertar_final("Canción D")
mi_lista.Buscar("Canción C")
mi_lista.mostrar_lista()