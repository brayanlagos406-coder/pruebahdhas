import math
p  = [4, 6]
vectores = [[3, 2],[-1, 5],[4, -3]]

x = vectores[0][0] + vectores[1][0] + vectores[2][0]
y = vectores[0][1] + vectores[1][1] + vectores[2][1]

neto = [x, y]
print("Desplazamiento neto:", neto)

final = [p[0] + x , p[1] + y]
print("Posición final:", final)

m1 = math.sqrt(vectores[0][0]**2 + vectores[0][1]**2)
m2 = math.sqrt(vectores[1][0]**2 + vectores[1][1]**2)
m3 = math.sqrt(vectores[2][0]**2 + vectores[2][1]**2)

magnitudes = [m1, m2, m3]

print("Magnitudes de los vectores:", magnitudes)
print("Magnitud del desplazamiento de V1:", round(m1, 2))
print("Magnitud del desplazamiento de V2:", round(m2, 2))
print("Magnitud del desplazamiento de V3:", round(m3, 2))

mayor_magnitud = max(magnitudes)
print("La mayor magnitud es:", round(mayor_magnitud, 2))

distancia_total = m1 + m2 + m3
print("La distancia total recorrida es:", round(distancia_total, 2))