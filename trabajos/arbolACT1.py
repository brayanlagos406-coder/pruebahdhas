# ACTIVIDAD 1: Árbol de problemas
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []  # Un árbol puede tener varios hijos

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def mostrar(self, nivel=0):  # Recursivo: procesar nodo -> procesar hijos
        print("    " * nivel + "- " + self.dato)
        for hijo in self.hijos:
            hijo.mostrar(nivel + 1)


# 1. Problema central
problema = Nodo("PROBLEMA: Baja capacidad para detectar oportunamente condiciones críticas")

# 2 y 3. Tres causas directas, cada una con una causa indirecta
causa1 = Nodo("Causa directa: Medición manual")
causa1.agregar_hijo(Nodo("Causa indirecta: Falta de instrumentos de medición"))

causa2 = Nodo("Causa directa: Registros dispersos")
causa2.agregar_hijo(Nodo("Causa indirecta: No existe un formato único de registro"))

causa3 = Nodo("Causa directa: Baja frecuencia de captura")
causa3.agregar_hijo(Nodo("Causa indirecta: Poco personal y parcelas muy distantes"))

# 4. Tres efectos
efecto1 = Nodo("Efecto: Decisiones tardías")
efecto2 = Nodo("Efecto: Desperdicio de agua")
efecto3 = Nodo("Efecto: Reducción de productividad")

# 5. Árbol: los efectos cuelgan del problema; las causas se muestran aparte
arbol_efectos = Nodo("EFECTOS")
for e in (efecto1, efecto2, efecto3):
    arbol_efectos.agregar_hijo(e)

arbol_causas = Nodo("CAUSAS")
for c in (causa1, causa2, causa3):
    arbol_causas.agregar_hijo(c)

print("=== ÁRBOL DE PROBLEMAS ===")
arbol_efectos.mostrar()
print()
print(problema.dato)
print()
arbol_causas.mostrar()

# 6. Justificación de dos relaciones
print("\n=== JUSTIFICACIÓN ===")
print("1. Medición manual -> problema: una persona solo mide cuando recorre "
    "las parcelas, por eso la condición crítica se detecta cuando ya ocurrió.")
print("2. Problema -> decisiones tardías: si la humedad baja no se detecta a "
    "tiempo, el riego se corrige tarde y el cultivo ya sufrió daño.")