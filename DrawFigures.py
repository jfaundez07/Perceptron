import random

def dibujar_circulo():
    # Inicializar una matriz de 10x10 con ceros
    matriz = [[0 for _ in range(10)] for _ in range(10)]
    
    # Generar un radio aleatorio que asegure que el círculo cabe en el espacio 10x10
    radio = random.randint(1, 4)
    
    # Generar coordenadas aleatorias para el centro del círculo
    centro_x = random.randint(radio, 9 - radio)
    centro_y = random.randint(radio, 9 - radio)
    
    # Usar la ecuación del círculo para determinar qué puntos de la matriz deben ser 1
    for x in range(10):
        for y in range(10):
            if (x - centro_x) ** 2 + (y - centro_y) ** 2 <= radio ** 2:
                matriz[x][y] = 1

    return matriz

def dibujar_linea():
    # Inicializar una matriz de 10x10 con ceros
    matriz = [[0 for _ in range(10)] for _ in range(10)]
    
    # Generar un largo aleatorio para la línea, de minimo 2
    largo = random.randint(2, 10)
    
    # Decidir aleatoriamente si la línea será vertical u horizontal
    es_vertical = random.choice([True, False])
    
    if es_vertical:
        # Generar una posición inicial aleatoria para la línea vertical
        inicio_x = random.randint(0, 9)
        inicio_y = random.randint(0, 10 - largo)
        
        # Dibujar la línea vertical en la matriz
        for i in range(largo):
            matriz[inicio_y + i][inicio_x] = 1
    else:
        # Generar una posición inicial aleatoria para la línea horizontal
        inicio_x = random.randint(0, 10 - largo)
        inicio_y = random.randint(0, 9)
        
        # Dibujar la línea horizontal en la matriz
        for i in range(largo):
            matriz[inicio_y][inicio_x + i] = 1
    
    return matriz

def matriz_a_vector(matriz):
    vector = [elemento for fila in matriz for elemento in fila]
    return vector

def imprimir_dibujo(matriz):
    print('\nDibujo:\n')
    for fila in matriz:
        print(' '.join(map(str, fila)))

def vector_a_matriz(vector):
    matriz = [vector[i:i + 10] for i in range(0, 100, 10)]
    return matriz