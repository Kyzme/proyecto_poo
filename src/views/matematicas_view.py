# Importamos la librería tkinter para crear interfaces gráficas
import tkinter as tk
from tkinter import messagebox  # Importamos el módulo para mostrar ventanas emergentes de alerta

# Función principal que solicita los datos al usuario a través de una ventana gráfica
# Recibe como parámetro una función `callback` que se ejecuta después de que el usuario ingresa los datos
def pedir_datos(callback):
    def calcular():
        try:
            # Intenta convertir los valores ingresados en los campos de texto
            x = float(x_entry.get())  # Entrada para x (en grados)
            numero = int(numero_entry.get())  # Grado de aproximación n

            # Validamos que n no sea excesivamente alto
            if numero > 20:
                messagebox.showerror("Error", "El grado de aproximación no puede ser mayor a 20.")
                return

            # Obtenemos la función seleccionada del menú desplegable
            funcion = funcion_var.get()
            a = 0  # Centro de la expansión de Taylor (usualmente 0)
            root.destroy()  # Cerramos la ventana actual
            callback(funcion, x, a, numero)  # Llamamos a la función controladora con los datos

        except ValueError:
            # Si hay error al convertir los datos, se muestra un mensaje de error
            messagebox.showerror("Error", "Ingresa valores válidos (x en grados, número entero).")

    # Creamos la ventana principal para ingresar datos
    root = tk.Tk()
    root.title("Cálculo - Serie de Taylor")

    # Centramos la ventana en la pantalla
    width, height = 800, 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_pos = int((screen_width - width) / 2)
    y_pos = int((screen_height - height) / 2)
    root.geometry(f"{width}x{height}+{x_pos}+{y_pos}")
    root.resizable(False, False)  # No se puede cambiar el tamaño de la ventana

    # Definimos colores personalizados para la interfaz
    bg_color = "#2e2e2e"  # Fondo oscuro
    fg_color = "#ffffff"  # Texto blanco
    entry_bg = "#444444"  # Fondo de entradas
    entry_fg = "#ffffff"  # Texto en entradas
    button_bg = "#555555"  # Fondo del botón

    # Aplicamos el color de fondo a la ventana principal
    root.configure(bg=bg_color)

    # Creamos un frame (contenedor) centralizado
    frame = tk.Frame(root, bg=bg_color)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Título del formulario
    tk.Label(frame, text="Cálculo por serie de Taylor", font=("Arial", 16, "bold"),
             bg=bg_color, fg=fg_color).grid(row=0, column=0, columnspan=2, pady=20)

    # Menú desplegable para seleccionar la función
    tk.Label(frame, text="Función:", bg=bg_color, fg=fg_color).grid(row=1, column=0, sticky="e", padx=10, pady=10)
    funcion_var = tk.StringVar(value="sin_custom")  # Valor por defecto

    funciones_disponibles = [
        "sin_custom", "cos_custom", "arcsen_custom",
        "arccos_custom", "senh_custom", "cosh_custom"
    ]

    funcion_menu = tk.OptionMenu(frame, funcion_var, *funciones_disponibles)
    funcion_menu.config(bg=entry_bg, fg=entry_fg, highlightthickness=0)
    funcion_menu.grid(row=1, column=1, padx=10, pady=10)

    # Campo de entrada para x (ángulo en grados)
    tk.Label(frame, text="x (grados):", bg=bg_color, fg=fg_color).grid(row=2, column=0, sticky="e", padx=10, pady=10)
    x_entry = tk.Entry(frame, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg)
    x_entry.grid(row=2, column=1, padx=10, pady=10)

    # Campo de entrada para el número de términos (n)
    tk.Label(frame, text="Grados de aproximación (n):", bg=bg_color, fg=fg_color).grid(row=3, column=0, sticky="e", padx=10, pady=10)
    numero_entry = tk.Entry(frame, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg)
    numero_entry.grid(row=3, column=1, padx=10, pady=10)

    # Botón para ejecutar el cálculo
    tk.Button(frame, text="Calcular", command=calcular,
              bg=button_bg, fg=fg_color, activebackground="#777777").grid(row=4, column=0, columnspan=2, pady=20)

    root.mainloop()  # Inicia el bucle principal de la interfaz

# Esta función muestra una nueva ventana con el resultado obtenido
def mostrar_resultado(resultado, x, numero):
    result_window = tk.Tk()
    result_window.title("Resultado")

    # Centramos la ventana de resultado
    width, height = 800, 600
    screen_width = result_window.winfo_screenwidth()
    screen_height = result_window.winfo_screenheight()
    x_pos = int((screen_width - width) / 2)
    y_pos = int((screen_height - height) / 2)
    result_window.geometry(f"{width}x{height}+{x_pos}+{y_pos}")
    result_window.resizable(False, False)

    # Definimos colores similares a la ventana anterior
    bg_color = "#2e2e2e"
    fg_color = "#ffffff"
    button_bg = "#555555"

    result_window.configure(bg=bg_color)

    frame = tk.Frame(result_window, bg=bg_color)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Mostramos el resultado en formato amigable
    texto = f"Resultado ≈ {resultado} usando {numero} términos de la serie de Taylor para x = {x}°"
    tk.Label(frame, text=texto, font=("Arial", 14), bg=bg_color, fg=fg_color).pack(padx=20, pady=40)

    # Botón para cerrar la ventana
    tk.Button(frame, text="Cerrar", command=result_window.destroy,
              bg=button_bg, fg=fg_color, activebackground="#777777").pack(pady=20)

    result_window.mainloop()
