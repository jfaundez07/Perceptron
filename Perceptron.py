import random
import math

# Clase del Perceptrón
class Perceptron:
    def __init__(self, tasa_aprendizaje):
        self.pesos_entrada = [generar_pesos(100) for _ in range(50)]
        self.pesos_oculta = [generar_pesos(50) for _ in range(2)]
        self.tasa_aprendizaje = tasa_aprendizaje

    def avanzar(self, entrada):
        # Capa de entrada a capa oculta
        salida_oculta = [funcion_escalon(suma_ponderada(entrada, self.pesos_entrada[i])) for i in range(50)]
        # Capa oculta a capa de salida
        salida_final = [suma_ponderada(salida_oculta, self.pesos_oculta[i]) for i in range(2)]
        # Aplicar softmax a la salida final
        return softmax(salida_final)

    def predecir(self, entrada):
        salida = self.avanzar(entrada)
        return salida.index(max(salida))
    
    def entrenar(self, entrada, etiqueta_real):
      
        salida_oculta = [funcion_escalon(suma_ponderada(entrada, self.pesos_entrada[i])) for i in range(50)]
        salida_final = [suma_ponderada(salida_oculta, self.pesos_oculta[i]) for i in range(2)]
        salida_softmax = softmax(salida_final)

        # Convertir etiqueta real a vector
        etiqueta_real_vector = [0, 0]
        etiqueta_real_vector[etiqueta_real] = 1

        # Calcular error en la capa de salida
        error_salida = [etiqueta_real_vector[i] - salida_softmax[i] for i in range(2)]

        # Actualizar pesos de la capa oculta a la capa de salida
        for i in range(2):
            for j in range(50):
                self.pesos_oculta[i][j] += self.tasa_aprendizaje * error_salida[i] * salida_oculta[j]

        # Calcular error en la capa oculta
        error_oculta = [0] * 50
        for i in range(50):
            for j in range(2):
                error_oculta[i] += error_salida[j] * self.pesos_oculta[j][i]

        # Actualizar pesos de la capa de entrada a la capa oculta
        for i in range(50):
            for j in range(100):
                self.pesos_entrada[i][j] += self.tasa_aprendizaje * error_oculta[i] * entrada[j]

def generar_pesos(n) -> list:
    pesos = []
    for _ in range(n):
        pesos.append(random.uniform(-1, 1))
    return pesos

def suma_ponderada(entradas, pesos) -> float:
    result = 0
    for x,w in zip(entradas, pesos):
        result += x*w
    return result

def funcion_escalon(valor) -> int:
    if valor > 0:
        return 1
    
    return 0

def softmax(entradas):
    exponenciales = []

    for i in entradas:
        exponenciales.append(math.exp(i)) # agrego los valores de e ^ i

    sum_exps = sum(exponenciales) # sumo todos los valores de e ^ i

    resultado = []

    for i in exponenciales:
        resultado.append(i / sum_exps)

    return resultado