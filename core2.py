class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []
        self.valor = 0.0


class Conexion:
    def __init__(self, nodo_a, nodo_b, resistencia):
        self.nodo_a = nodo_a
        self.nodo_b = nodo_b
        self.resistencia = resistencia
        self.voltaje = 0.0


def calcular_voltajes(raiz):
    cola = [raiz]
    visitados = set()

    while cola:
        nodo_actual = cola.pop(0)
        visitados.add(nodo_actual)

        for conexion in nodo_actual.conexiones:
            otro_nodo = conexion.nodo_a if conexion.nodo_b == nodo_actual else conexion.nodo_b

            if otro_nodo not in visitados:
                conexion.voltaje = abs(nodo_actual.valor - otro_nodo.valor)
                otro_nodo.valor = nodo_actual.valor / conexion.resistencia
                cola.append(otro_nodo)


def calcular_resistencia_total(raiz):
    resistencia_total = 0.0
    visitados = set()

    def calcular_resistencia(nodo_actual):
        nonlocal resistencia_total
        visitados.add(nodo_actual)

        for conexion in nodo_actual.conexiones:
            otro_nodo = conexion.nodo_a if conexion.nodo_b == nodo_actual else conexion.nodo_b

            if otro_nodo not in visitados:
                resistencia_total += conexion.resistencia
                calcular_resistencia(otro_nodo)

    calcular_resistencia(raiz)
    return resistencia_total


def determinar_tipo_resistencias(raiz):
    tipo_resistencias = None
    visitados = set()

    def dfs(nodo_actual, tipo):
        nonlocal tipo_resistencias
        visitados.add(nodo_actual)

        for conexion in nodo_actual.conexiones:
            otro_nodo = conexion.nodo_a if conexion.nodo_b == nodo_actual else conexion.nodo_b

            if otro_nodo not in visitados:
                if tipo_resistencias is None:
                    tipo_resistencias = tipo
                elif tipo_resistencias != tipo:
                    tipo_resistencias = "Mixto"
                    return

                dfs(otro_nodo, tipo)

    dfs(raiz, "Serie" if raiz.valor == 0.0 else "Paralelo")
    return tipo_resistencias


def calcular_corrientes(raiz, intensidad_fuente):
    corrientes = {}

    def dfs(nodo_actual):
        corrientes[nodo_actual.nombre] = nodo_actual.valor * intensidad_fuente

        for conexion in nodo_actual.conexiones:
            otro_nodo = conexion.nodo_a if conexion.nodo_b == nodo_actual else conexion.nodo_b

            if otro_nodo.nombre not in corrientes:
                dfs(otro_nodo)

    dfs(raiz)
    return corrientes


# Crear nodos
nodo1 = Nodo("Nodo 1")
nodo2 = Nodo("Nodo 2")
nodo3 = Nodo("Nodo 3")

# Crear conexiones
conexion1 = Conexion(nodo1, nodo2, 2.0)
conexion2 = Conexion(nodo2, nodo3, 3.0)

# Agregar conexiones a los nodos
nodo1.conexiones.append(conexion1)
nodo2.conexiones.extend([conexion1, conexion2])
nodo3.conexiones.append(conexion2)

# Establecer la fuente de voltaje en el primer nodo
nodo1.valor = 5.0

# Calcular los voltajes en los nodos restantes
calcular_voltajes(nodo1)

# Imprimir los voltajes en cada nodo
print("Voltaje en el Nodo 1:", nodo1.valor)
print("Voltaje en el Nodo 2:", nodo2.valor)
print("Voltaje en el Nodo 3:", nodo3.valor)

# Calcular la resistencia total
resistencia_total = calcular_resistencia_total(nodo1)
print("Resistencia total:", resistencia_total)

# Imprimir el valor y el voltaje de las resistencias
for i, conexion in enumerate(nodo1.conexiones):
    print("Resistencia", i + 1, "- Valor:", conexion.resistencia, "- Voltaje:", conexion.voltaje)

# Determinar el tipo de resistencias
tipo_resistencias = determinar_tipo_resistencias(nodo1)
print("Tipo de resistencias:", tipo_resistencias)

# Calcular las corrientes
intensidad_fuente = 2.5  # Intensidad de corriente de la fuente
corrientes = calcular_corrientes(nodo1, intensidad_fuente)
for nodo, corriente in corrientes.items():
    print("Corriente en", nodo + ":", corriente)
