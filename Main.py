import random
import DrawFigures as df
import Perceptron as pc

def main():

    perceptron = pc.Perceptron(0.001)

    # Entrenamiento del perceptrón
    for iteracion in range(50):

        # 30 iteraciones de entrenamiento con imágenes de líneas rectas
        for _ in range(30):
            matriz = df.dibujar_circulo()
            vector = df.matriz_a_vector(matriz)
            perceptron.entrenar(vector, 0)
        
        # 30 iteraciones de entrenamiento con imágenes de líneas circulares
        for _ in range(30):
            matriz = df.dibujar_linea()
            vector = df.matriz_a_vector(matriz)
            perceptron.entrenar(vector, 1)
    
    contador_aciertos =0

    # Prueba del perceptrón
    for _ in range(100): 
        if random.choice([True, False]):
            matriz = df.dibujar_circulo()
            etiqueta_real = 0
        else:
            matriz = df.dibujar_linea()
            etiqueta_real = 1

        vector = df.matriz_a_vector(matriz)
        prediccion = perceptron.predecir(vector)
        print(f'Etiqueta real: {etiqueta_real}, Predicción: {prediccion}')

        if etiqueta_real == prediccion:
            contador_aciertos += 1

    print(f'Número de aciertos: {contador_aciertos}/100')

main()
