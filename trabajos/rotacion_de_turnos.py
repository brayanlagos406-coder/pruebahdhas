#resolver el problema de rotacion de turnos, se debe crear una lista circular y luego rotarla segun la cantidad de turnos que se deseen rotar.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        

class ListaCircular:
    def __init__(self):
        self.cabeza = None
        
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            nuevo.siguiente = nuevo  # Apunta a sí mismo
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:  # Encuentra el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo  # El último nodo apunta al nuevo nodo
            nuevo.siguiente = self.cabeza  # El nuevo nodo apunta a la cabeza
            self.cabeza = nuevo  # La cabeza ahora es el nuevo nodo
            
    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            nuevo.siguiente = nuevo  # Apunta a sí mismo
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:  # Encuentra el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo  # El último nodo apunta al nuevo nodo
            nuevo.siguiente = self.cabeza  # El nuevo nodo apunta a la cabeza
                        
    def mostrar_lista(self):
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        
        actual = self.cabeza
        while True:
            print(f"[{actual.dato}]-> ", end="")
            actual = actual.siguiente
            if actual == self.cabeza:  # Si volvemos a la cabeza, terminamos
                break
        print("fin de la lista")
    
    def rotar(self, cantidad):
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        
        for _ in range(cantidad):
            self.cabeza = self.cabeza.siguiente  # Mueve la cabeza al siguiente nodo
        
        
    def buscar(self, dato):
        if self.cabeza is None:
            print("La lista está vacía.")
            return False
        
        actual = self.cabeza
        while True:
            if actual.dato == dato:
                print(f"El dato '{dato}' fue encontrado en la lista.")
                return True
            actual = actual.siguiente
            if actual == self.cabeza:  # Si volvemos a la cabeza, terminamos
                break
        
        print(f"El dato '{dato}' no fue encontrado en la lista.")
        return False
    
    def eliminar(self, dato):
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        
        actual = self.cabeza
        anterior = None
        
        while True:
            if actual.dato == dato:
                if anterior is None:  # Si es el primer nodo
                    # Encontrar el último nodo para actualizar su siguiente
                    ultimo = self.cabeza
                    while ultimo.siguiente != self.cabeza:
                        ultimo = ultimo.siguiente
                    if actual.siguiente == self.cabeza:  # Si es el único nodo
                        self.cabeza = None
                    else:
                        ultimo.siguiente = actual.siguiente
                        self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                
                print(f"El dato '{dato}' fue eliminado de la lista.")
                return
            
            anterior = actual
            actual = actual.siguiente
            
            if actual == self.cabeza:  # Si volvemos a la cabeza, terminamos
                break
        
        print(f"El dato '{dato}' no fue encontrado en la lista.")
    


    