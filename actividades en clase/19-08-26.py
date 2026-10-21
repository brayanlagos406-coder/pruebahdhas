class Nodo:
    def __init__(self, dato):  # Inicializa un nodo con un dato y un puntero al siguiente nodo
        # Cada nodo guarda el valor y una referencia al siguiente nodo
        self.dato = dato
        self.siguiente = None  # puntero al siguiente nodo


# Clase que controla la lista enlazada simple
class ListaSimple:
    def __init__(self):
        # La cabeza apunta al primer nodo de la lista
        # Si la lista está vacía, se queda en None
        self.cabeza = None

    # Inserta un nuevo dato al inicio de la lista
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)              # crea el nuevo nodo
        nuevo.siguiente = self.cabeza   # apunta al nodo que antes era el primero
        self.cabeza = nuevo             # ahora el nuevo nodo es la cabeza

    # Inserta un nuevo dato al final de la lista
    def insertar_final(self, dato):
        nuevo = Nodo(dato)              # crea el nuevo nodo

        # Si la lista está vacía, el nuevo nodo pasa a ser la cabeza
        if self.cabeza is None:
            self.cabeza = nuevo
            return

        # Recorrer desde la cabeza hasta el último nodo
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente

        # Enlaza el último nodo con el nuevo nodo
        actual.siguiente = nuevo

    # Muestra todos los elementos de la lista
    def mostrar_lista(self):
        actual = self.cabeza

        # Mientras haya nodos, se imprimen uno por uno
        while actual is not None:
            print(f"[{actual.dato}]-> ", end="") # Imprime el dato del nodo actual y una flecha
            actual = actual.siguiente

        print("fin de la lista")

    # Inserta un dato en una posición específica dentro de la lista
    def insertarEnPosc(self, dato, posicion):
        
        nuevo = Nodo(dato)  # crea el nuevo nodo

        # Si la posición es 0, se inserta al inicio
        if posicion == 0:
            self.insertar_inicio(dato)
            return

        actual = self.cabeza
        indice = 0

        # Recorre la lista hasta llegar a la posición deseada o al final de la lista
        while actual is not None and indice < posicion - 1:
            actual = actual.siguiente
            indice += 1

        # Si se llegó al final de la lista antes de alcanzar la posición, se inserta al final
        if actual is None:
            self.insertar_final(dato)
            return

        # Inserta el nuevo nodo en la posición deseada
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo
        
        #____________________________________________________________________________________________________
        
    def insertar_medio(self, dato, posicion):
        nuevo = Nodo(dato)  # crea el nuevo nodo
        actual = self.cabeza # puntero al primer nodo de la lista
        while actual is not None: # recorre la lista hasta encontrar la posición deseada
            
            if actual.dato == posicion: # si el dato del nodo actual es igual a la posición deseada, se inserta el nuevo nodo después de este
                break
            actual = actual.siguiente # si no se encuentra la posición, se sigue recorriendo la lista
            
        
        if actual is not None: # si no se encontró la posición deseada, se imprime un mensaje de error
            nuevo.siguiente = actual.siguiente # el nuevo nodo apunta al siguiente nodo del actual
            actual.siguiente = nuevo # el nodo actual apunta al nuevo nodo
        else:
            print("No se encontró la posición especificada, se insertara al inicio.")
            mis_tareas.insertar_inicio(dato)
        #return False
        

    # Busca si un dato existe dentro de la lista
    def buscar(self, dato):
        actual = self.cabeza

        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente

        return False
    # Elimina un nodo que contiene un dato específico
    def eliminar(self, dato):
        actual = self.cabeza
        
        if actual.dato == dato: # si se encuentra el nodo con el dato especificado
                
            if actual == self.cabeza: # si el nodo a eliminar es la cabeza, se actualiza la cabeza al siguiente nodo
                    self.cabeza = actual.siguiente # mueve la cabeza al siguiente nodo
        else: # si el nodo a eliminar no es la cabeza, se busca el nodo anterior para actualizar su referencia
            while actual is not None: # recorre la lista hasta encontrar el nodo anterior al que contiene el dato a eliminar
                if actual.siguiente and actual.siguiente.dato == dato: # si el siguiente nodo contiene el dato a eliminar
                    actual.siguiente = actual.siguiente.siguiente # se salta el nodo a eliminar
                    break
                actual = actual.siguiente
        

    


# Prueba del sistema de tareas
mis_tareas = ListaSimple()
mis_tareas.insertar_inicio("q")
mis_tareas.insertar_final("b")
mis_tareas.insertar_final("c")
mis_tareas.insertar_final("d")
mis_tareas.insertar_final("e")
mis_tareas.insertar_medio("a", "c")
mis_tareas.eliminar("d")
mis_tareas.mostrar_lista()