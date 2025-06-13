# Importa la clase del modelo(models) que realiza los cálculos matemáticos (Serie de Taylor)
from src.models.matematicas_model import SerieTaylor

# Importa funciones de la vista(views) para interactuar con el usuario
from src.views.matematicas_view import pedir_datos, mostrar_resultado

# Controlador(controllers) principal que conecta la vista con el modelo
class UserController:
    def ejecutar(self):
        # Función de callback que se ejecuta cuando el usuario ingresa los datos desde la vista
        def callback(funcion, x, a, numero):
            # Instanciamos el modelo matemático
            modelo = SerieTaylor()
            # Convertimos el valor de x de grados a radianes
            x_rad = modelo.grados_a_radianes(x)
            # Calculamos el resultado usando el modelo
            resultado = modelo.calcular(funcion, x_rad, a, numero)
            # Mostramos el resultado al usuario usando la función de la vista
            mostrar_resultado(resultado, x, numero)

        # Llamamos a la vista para pedir los datos al usuario
        # Una vez que el usuario los ingrese, se ejecuta automáticamente la función callback
        pedir_datos(callback)
