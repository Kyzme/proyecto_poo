# Importa la clase UserController desde el archivo matematicas_controller.py que está dentro de src/controllers
from src.controllers.matematicas_controller import UserController

if __name__ == "__main__": # Punto de entrada principal del programa
    src = UserController() # Crea una instancia del controlador principal
    src.ejecutar() # Llama al método principal para iniciar la aplicación
