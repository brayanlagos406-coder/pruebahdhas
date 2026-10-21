class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None  # Atributo para apuntar al nodo anterior
        self.ultimo = None  # Atributo para apuntar al último nodo

class listacircular:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None  # Atributo para apuntar al último nodo
        self.anterior = None  # Atributo para apuntar al nodo anterior
        

    def insertar_inicio(self, dato):
        nuevo = nodo(dato)
        if self.cabeza is None:
            nuevo.siguiente = nuevo  # Apunta a sí mismo
            
            self.cabeza = nuevo
            return
        
        ultimo = self.cabeza
        
        while ultimo.siguiente != self.cabeza:  # Encuentra el último nodo
            ultimo = ultimo.siguiente
        
        nuevo.siguiente = self.cabeza  # El nuevo nodo apunta a la cabeza
        ultimo.siguiente = nuevo  # El último nodo apunta al nuevo nodo
        self.cabeza = nuevo  # La cabeza ahora es el nuevo nodo
        
    def Eliminar(self, dato):
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        
        actual = self.cabeza
        anterior = None
        
        while True: # Bucle infinito hasta encontrar el nodo o volver a la cabeza
            if actual.dato == dato:
                # Caso especial: solo hay un nodo en la lista
                if actual == self.cabeza and actual.siguiente == self.cabeza:
                    self.cabeza = None
                    print(f"Elemento {dato} eliminado.")
                    return # volver a la función después de eliminar el nodo

                if anterior is not None: # Si no estamos eliminando la cabeza, simplemente ajustamos el puntero del nodo anterior
                    anterior.siguiente = actual.siguiente
                else: 
                    # Si estamos eliminando la cabeza, necesitamos encontrar el último nodo
                    ultimo = self.cabeza
                    while ultimo.siguiente != self.cabeza: # Encuentra el último nodo
                        ultimo = ultimo.siguiente
                    ultimo.siguiente = actual.siguiente
                    self.cabeza = actual.siguiente  # Actualizamos la cabeza
                
                print(f"Elemento {dato} eliminado.")
                return
            
            anterior = actual
            actual = actual.siguiente
            
            if actual == self.cabeza:  # Si volvemos a la cabeza, terminamos
                break
        
        print(f"Elemento {dato} no encontrado en la lista.")
        

    def Modificar(self, dato_viejo, dato_nuevo): # método para modificar un nodo existente en la lista
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        
        actual = self.cabeza # iniciamos la búsqueda desde la cabeza de la lista
        
        while True: # Bucle infinito hasta encontrar el nodo o volver a la cabeza
            if actual.dato == dato_viejo:
                actual.dato = dato_nuevo
                print(f"Elemento {dato_viejo} modificado a {dato_nuevo}.")
                return
            
            actual = actual.siguiente # avanzamos al siguiente nodo
            
            if actual == self.cabeza:  # Si volvemos a la cabeza, terminamos
                break
        
        print(f"Elemento {dato_viejo} no encontrado en la lista.")
        
    def mostrar_lista(self):
        if self.cabeza is None:
            print("La lista está vacía.")
            return

        
        actual = self.cabeza
        while True:
            print(f"[{actual.dato}]-> ", end=" ")
            actual = actual.siguiente
            if actual == self.cabeza:  # Si volvemos a la cabeza, terminamos
                break
            
        print("fin de la lista")
        
        
        
        
        
        
        
        
        
mi_lista = listacircular()
mi_lista.insertar_inicio("Canción B")
mi_lista.insertar_inicio("Canción A")
mi_lista.insertar_inicio("Canción C")
mi_lista.insertar_inicio("Canción D")
mi_lista.insertar_inicio("Canción E")   
mi_lista.Modificar("Canción C", "Canción F")
mi_lista.mostrar_lista()