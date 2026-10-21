class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # Puntero


class RondaAgentes:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.turno = None

    def lista_vacia(self):
        if self.cabeza == None:
            return True
        return False

    def siguiente_agente(self):
        if self.turno is None:
            return None

        agente = self.turno.dato

        print(f"Turno actual: {agente}")

        self.turno = self.turno.siguiente

        print(f"Quién toma el siguiente turno: {self.turno.dato}")

        return agente

    def insertar_final_optimizado(self, agente):
        nuevo_agente = Nodo(agente)

        if self.lista_vacia():
            self.cabeza = self.ultimo = self.turno = nuevo_agente
            nuevo_agente.siguiente = nuevo_agente
            return

        nuevo_agente.siguiente = self.cabeza
        self.ultimo.siguiente = nuevo_agente
        self.ultimo = nuevo_agente

    def eliminar_agente(self, agente):
        if self.lista_vacia():
            return

        actual = self.cabeza
        anterior = self.ultimo

        while True:

            if actual.dato == agente:

                # Si solamente queda un agente
                if actual == anterior:
                    self.cabeza = None
                    self.ultimo = None
                    self.turno = None
                    return

                # Si eliminamos la cabeza
                if actual == self.cabeza:
                    self.cabeza = actual.siguiente
                    self.ultimo.siguiente = self.cabeza

                else:
                    anterior.siguiente = actual.siguiente

                    # Si eliminamos el último
                    if actual == self.ultimo:
                        self.ultimo = anterior

                # Si el eliminado tenía el turno
                if self.turno == actual:
                    self.turno = actual.siguiente

                return

            anterior = actual
            actual = actual.siguiente

            if actual == self.cabeza:
                return
    def mostrar_agentes(self):
        if self.lista_vacia():
            print("No hay agentes en la lista.")
            return

        actual = self.cabeza
        while True:
            print(f"[{actual.dato}] -> ", end="")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("fin de la lista")
            
# Crear la ronda
ronda = RondaAgentes()

# Agregar los agentes
ronda.insertar_final_optimizado("Ana")
ronda.insertar_final_optimizado("Bruno")
ronda.insertar_final_optimizado("Carla")
ronda.insertar_final_optimizado("Diego")

# Simular 10 solicitudes
for i in range(1, 11):

    print(f"\nSolicitud {i}")

    agente = ronda.siguiente_agente()

    # Después de la solicitud 5 se elimina a Bruno
    if i == 5:
        print("\n--- Eliminando a Bruno ---")
        ronda.eliminar_agente("Bruno")