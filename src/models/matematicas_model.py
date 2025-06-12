class SerieTaylor:
    # Método para calcular el factorial de un número (n!)
    def factorial(self, numero):
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i  # Multiplica sucesivamente desde 1 hasta 'numero'
        return resultado

    # Método para calcular una potencia (base^exponente)
    def potencia(self, base, exponente):
        resultado = 1
        for _ in range(exponente):
            resultado *= base  # Multiplica la base por sí misma 'exponente' veces
        return resultado

    # Método que aproxima el seno de 'x' usando la serie de Taylor con 'numero' de términos
    def sin_custom(self, x, numero):
        resultado = 0  # Acumula el resultado de la serie
        for i in range(numero):
            signo = 1 if i % 2 == 0 else -1  # Alterna signo: + - + - ... (equivale a (-1)^i)
            numerador = signo * self.potencia(x, 2 * i + 1)  # Calcula x^(2i+1) con su signo
            denominador = self.factorial(2 * i + 1)  # Calcula (2i+1)!
            resultado += numerador / denominador  # Suma el término actual a la aproximación
        return resultado

    # Método general para elegir qué función calcular (por ahora solo sin_custom con a=0)
    def calcular(self, funcion, x, a, numero):
        if funcion == 'sin_custom' and a == 0:
            return self.sin_custom(x, numero)  # Llama a sin_custom si se cumplen las condiciones
        else:
            raise ValueError("Solo se admite sin_custom con a=0")  # Restringe el uso a sin(x) centrado en 0

    # Convierte un ángulo en grados a radianes
    def grados_a_radianes(self, grados):
        return grados * (3.141592653589793 / 180)  # Fórmula para conversión: rad = deg × π / 180
