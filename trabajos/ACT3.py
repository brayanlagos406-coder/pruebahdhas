# ACTIVIDAD 3: Escenario de simulación
# 1. CONTEXTO Y PROBLEMA CENTRAL
#    Asociación de productores de fresa que riega por turnos y no sabe a tiempo
#    cuándo el suelo está seco ni cuándo se vacía el tanque.
#    Problema: baja capacidad para detectar a tiempo humedad crítica y bajo
#    nivel de agua en el tanque de riego.
#
# 2. VARIABLES: humedad (%), temperatura (°C), nivel del tanque (%),
#    precipitación (lluvia sí/no), estado de la parcela, hora de medición.
#
# 3. ENTIDADES: Finca, Zona, Parcela, Sensor, Medición, Alerta, Productor.
#
# 4. ESTRUCTURA PRINCIPAL: árbol Finca -> Zonas -> Parcelas (relación jerárquica),
#    con una lista de mediciones por parcela y una cola de alertas.
#
# 5. OPERACIONES: insertar medición, buscar parcela, recorrer el árbol,
#    promedio por zona, generar alerta, atender la siguiente alerta.
#
# 6. DATOS SIMULADOS: humedad baja entre 1 y 4 puntos por hora y sube 8 con lluvia
#    (15 % de probabilidad por hora); temperatura sigue el ciclo del día;
#    el riego sube la humedad y gasta agua del tanque.

import random


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # Puntero


class ListaMediciones:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None

    def lista_vacia(self):
        return self.cabeza is None

    def insertar_final(self, medicion):
        nuevo = Nodo(medicion)
        if self.lista_vacia():
            self.cabeza = self.ultimo = nuevo
            return
        self.ultimo.siguiente = nuevo
        self.ultimo = nuevo

    def promedio_humedad(self):
        actual = self.cabeza
        suma = 0
        cantidad = 0
        while actual is not None:
            suma += actual.dato["humedad"]
            cantidad += 1
            actual = actual.siguiente
        return suma / cantidad if cantidad > 0 else 0


class ColaAlertas:
    def __init__(self):
        self.frente = None
        self.final = None
        self.cantidad = 0

    def cola_vacia(self):
        return self.frente is None

    def encolar(self, alerta):
        nuevo = Nodo(alerta)
        if self.cola_vacia():
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        self.cantidad += 1

    def desencolar(self):
        if self.cola_vacia():
            return None
        alerta = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.cantidad -= 1
        return alerta

    def mas_antigua(self):
        return None if self.cola_vacia() else self.frente.dato


class Parcela:
    def __init__(self, id_parcela):
        self.id = id_parcela
        self.humedad = random.randint(30, 45)
        self.temperatura = 20.0
        self.estado = "normal"
        self.mediciones = ListaMediciones()


class Zona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.parcelas = []

    def promedio_humedad(self):
        suma = 0
        for p in self.parcelas:
            suma += p.humedad
        return suma / len(self.parcelas)


class Finca:
    def __init__(self):
        self.zonas = []
        self.tanque = 100
        self.alertas = ColaAlertas()
        for z in range(1, 3):
            zona = Zona(f"Zona {z}")
            for p in range(1, 11):
                zona.parcelas.append(Parcela(f"P{(z - 1) * 10 + p}"))
            self.zonas.append(zona)

    def buscar_parcela(self, id_parcela):
        for zona in self.zonas:
            for p in zona.parcelas:
                if p.id == id_parcela:
                    return p
        return None

    def simular_hora(self, hora):
        lluvia = random.random() < 0.15
        for zona in self.zonas:
            for p in zona.parcelas:
                if lluvia:
                    p.humedad += 8
                else:
                    p.humedad -= random.randint(1, 4)
                p.humedad = max(0, min(100, p.humedad))
                p.temperatura = round(15 + 10 * (1 - abs(hora - 13) / 13) + random.uniform(-2, 2), 1)

                p.mediciones.insertar_final({"hora": hora, "humedad": p.humedad,
                                            "temperatura": p.temperatura})

                if p.humedad < 25:
                    p.estado = "crítico"
                    self.alertas.encolar((hora, p.id, "Humedad crítica"))
                    p.humedad += 15          # Riego
                    self.tanque -= 3
                else:
                    p.estado = "normal"

        if lluvia:
            self.tanque = min(100, self.tanque + 10)
        if self.tanque < 20:
            self.alertas.encolar((hora, "Tanque", "Nivel bajo"))

    # Pregunta 1: ¿qué parcelas tienen humedad crítica en este momento?
    def parcelas_criticas(self):
        criticas = []
        for zona in self.zonas:
            for p in zona.parcelas:
                if p.estado == "crítico":
                    criticas.append(p.id)
        return criticas

    # Pregunta 2: ¿cuántas alertas sin atender hay y cuál es la más antigua?
    def resumen_alertas(self):
        return self.alertas.cantidad, self.alertas.mas_antigua()


# ---------- SIMULACIÓN ----------
random.seed(1)
finca = Finca()

for hora in range(6, 19):
    finca.simular_hora(hora)

print("=== RESULTADOS DE LA SIMULACIÓN ===")
print("Pregunta 1 - Parcelas con humedad crítica:", finca.parcelas_criticas())
cantidad, antigua = finca.resumen_alertas()
print("Pregunta 2 - Alertas sin atender:", cantidad)
print("             Alerta más antigua:", antigua)
print("Nivel del tanque:", finca.tanque, "%")
for zona in finca.zonas:
    print(f"Humedad promedio {zona.nombre}: {zona.promedio_humedad():.1f} %")

print("\n=== ATENDIENDO LAS 3 PRIMERAS ALERTAS ===")
for _ in range(3):
    alerta = finca.alertas.desencolar()
    if alerta is not None:
        print(f"Hora {alerta[0]} | {alerta[1]} | {alerta[2]}")