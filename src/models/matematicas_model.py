class SerieTaylor:
    # Función factorial: n! = 1 × 2 × 3 × ... × n
    def factorial(self, numero):
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

    # Función potencia: base^exponente = base * base * ... * base (exponente veces)
    def potencia(self, base, exponente):
        resultado = 1
        for _ in range(exponente):
            resultado *= base
        return resultado

    # ------------------ FUNCIONES DE TAYLOR ------------------

    # Serie de Taylor para sin(x) alrededor de 0:
    # sin(x) ≈ ∑ [(-1)^n * x^(2n+1)] / (2n+1)!    para n = 0 hasta número
    def sin_custom(self, x, numero):
        resultado = 0
        for i in range(numero):
            signo = 1 if i % 2 == 0 else -1 # Alternancia de signo: (-1)^i
            numerador = signo * self.potencia(x, 2 * i + 1) # x^(2i+1)
            denominador = self.factorial(2 * i + 1) # (2i+1)!
            resultado += numerador / denominador
        return resultado

    # Serie de Taylor para cos(x) alrededor de 0:
    # cos(x) ≈ ∑ [(-1)^n * x^(2n)] / (2n)!    para n = 0 hasta número
    def cos_custom(self, x, numero):
        resultado = 0
        for i in range(numero):
            signo = 1 if i % 2 == 0 else -1 # Alternancia de signo: (-1)^i
            numerador = signo * self.potencia(x, 2 * i) # x^(2i)
            denominador = self.factorial(2 * i) # (2i)!
            resultado += numerador / denominador
        return resultado

    # Serie de Taylor para arcsin(x), conocida como expansión de Maclaurin:
    # arcsin(x) ≈ ∑ [(2n)! / (4^n * (n!)^2 * (2n+1))] * x^(2n+1)
    def arcsen_custom(self, x, numero):
        resultado = 0
        for n in range(numero):
            numerador = self.factorial(2 * n) * self.potencia(x, 2 * n + 1) # (2n)! * x^(2n+1)
            denominador = self.potencia(4, n) * self.potencia(self.factorial(n), 2) * (2 * n + 1) # 4^n # (n!)^2 # (2n+1)
            resultado += numerador / denominador
        return resultado

    # Serie para arccos(x): se define como arccos(x) = π/2 - arcsin(x)
    def arccos_custom(self, x, numero):
        pi_sobre_dos = 3.141592653589793 / 2
        return pi_sobre_dos - self.arcsen_custom(x, numero)

    # Serie de Taylor para sinh(x) alrededor de 0:
    # sinh(x) ≈ ∑ [x^(2n+1)] / (2n+1)!    para n = 0 hasta número
    def senh_custom(self, x, numero):
        resultado = 0
        for i in range(numero):
            numerador = self.potencia(x, 2 * i + 1) # x^(2i+1)
            denominador = self.factorial(2 * i + 1) # (2i+1)!
            resultado += numerador / denominador
        return resultado

    # Serie de Taylor para cosh(x) alrededor de 0:
    # cosh(x) ≈ ∑ [x^(2n)] / (2n)!     para n = 0 hasta número
    def cosh_custom(self, x, numero):
        resultado = 0
        for i in range(numero):
            numerador = self.potencia(x, 2 * i) # x^(2i)
            denominador = self.factorial(2 * i) # (2i)!
            resultado += numerador / denominador
        return resultado

    # Método general para llamar una función específica según su nombre
    def calcular(self, funcion, x, a, numero):
        # Solo acepta expansiones centradas en 0 por ahora
        if a != 0:
            raise ValueError("Solo se admite expansión centrada en 0")
        # Diccionario que asocia el nombre con la función correspondiente
        funciones = {
            'sin_custom': self.sin_custom,
            'cos_custom': self.cos_custom,
            'arcsen_custom': self.arcsen_custom,
            'arccos_custom': self.arccos_custom,
            'senh_custom': self.senh_custom,
            'cosh_custom': self.cosh_custom
        }
        # Verifica si la función existe y la ejecuta con los parámetros
        if funcion in funciones:
            return funciones[funcion](x, numero)
        else:
            raise ValueError("Función no reconocida")

    # Conversión de grados a radianes, porque las funciones trigonométricas en Taylor
    # se definen para radianes, no grados.
    def grados_a_radianes(self, grados):
        return grados * (3.141592653589793 / 180)
