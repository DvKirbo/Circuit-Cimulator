import numpy as np

# Obtener el número de nodos del circuito
n = int(input("Ingrese el número de nodos: "))

# Obtener el número de fuentes de voltaje
num_fuentes_voltaje = int(input("Ingrese la cantidad de fuentes de voltaje: "))

# Obtener el número de resistencias3
num_resistencias = int(input("Ingrese la cantidad de resistencias: "))

# Crear una lista vacía para almacenar las resistencias
resistencias = []

# Crear una lista vacía para almacenar las fuentes de corriente
corrientes = []

# Crear una lista vacía para almacenar las fuentes de voltaje
voltajes = []

# Leer los valores de las resistencias
for i in range(num_resistencias):
    resistencia = float(input(f"Ingrese el valor de la resistencia {i+1}: "))
    resistencias.append(resistencia)

# Leer los valores de las fuentes de corriente
for i in range(n-1):
    corriente = float(input(f"Ingrese el valor de la corriente {i+1}: "))
    corrientes.append(corriente)

# Leer los valores de las fuentes de voltaje
for i in range(num_fuentes_voltaje):
    voltaje = float(input(f"Ingrese el valor del voltaje {i+1}: "))
    voltajes.append(voltaje)

# Construir la matriz 'a' y el vector 'b' dinámicamente
a = np.zeros((n, n))
b = np.zeros(n)

for i in range(n):
    for j in range(n):
        if i == j:
            # Sumar los conductancias de las resistencias conectadas al nodo i
            for resistencia in resistencias:
                a[i][i] += 1/resistencia
        else:
            # Restar la conductancia de la resistencia conectada entre los nodos i y j
            a[i][j] = -1/resistencias[j]
            a[i][i] += 1/resistencias[j]

    if i < n-1:
        # Asignar el valor de la fuente de corriente al vector 'b'
        b[i] = corrientes[i]
    else:
        # Agregar la contribución de las fuentes de voltaje al vector 'b'
        for j in range(num_fuentes_voltaje):
            b[i] -= a[i][j] * voltajes[j]

# Resolver el sistema de ecuaciones
solucion = np.linalg.solve(a, b)

# Imprimir los voltajes y corrientes
for i in range(n):
    if i == 0:
        print(f"Voltaje en el nodo {i}: {solucion[i]:.2f} V (Referencia)")
    else:
        print(f"Voltaje en el nodo {i}: {solucion[i]:.2f} V")

for i in range(n-1):
    print(f"Corriente en la fuente {i+1}: {corrientes[i]:.2f} A")

for i in range(num_fuentes_voltaje):
    print(f"Voltaje en la fuente de voltaje {i+1}: {voltajes[i]:.2f} V")
