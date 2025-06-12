#Este archivo ya es mas que todo para darle una interfaz grafica al programa con la libreria de tkinter
import tkinter as tk
from tkinter import messagebox

# Función que se encarga de pedir los datos al usuario mediante la interfaz gráfica
# Recibe como argumento una función 'callback' que se ejecutará al finalizar la entrada de datos
def pedir_datos(callback):
    # Función interna que se ejecuta al hacer clic en el botón de calcular
    def calcular():
        try:
            # Obtiene el valor de x (en grados) desde el campo de entrada y lo convierte a float
            x = float(x_entry.get())
            # Obtiene el número de términos de la serie y lo convierte a entero
            numero = int(numero_entry.get())
            # Valida que el número de términos no sea excesivo (máx. 20)
            if numero > 20:
                messagebox.showerror("Error", "El grado de aproximación no puede ser mayor a 20.")
                return # Si hay error, no continúa
            # Define los parámetros fijos por ahora: se calcula seno centrado en a=0
            funcion = "sin_custom"
            a = 0
            # Cierra la ventana de entrada de datos
            root.destroy()
            # Llama a la función callback con los valores obtenidos
            callback(funcion, x, a, numero)
        except ValueError:
            # Si ocurre un error al convertir los datos, se muestra un mensaje de error
            messagebox.showerror("Error", "Ingresa valores válidos (x en grados, número entero).")

    root = tk.Tk()
    root.title("Cálculo - Serie de Taylor")

    # Tamaño fijo y centrado
    width, height = 800, 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_pos = int((screen_width - width) / 2)
    y_pos = int((screen_height - height) / 2)
    root.geometry(f"{width}x{height}+{x_pos}+{y_pos}")
    root.resizable(False, False)

    # Modo oscuro
    bg_color = "#2e2e2e"
    fg_color = "#ffffff"
    entry_bg = "#444444"
    entry_fg = "#ffffff"
    button_bg = "#555555"

    root.configure(bg=bg_color)

    # Frame central
    frame = tk.Frame(root, bg=bg_color)
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Centramos el contenido

    # Título
    tk.Label(frame, text="Cálculo de sin(x) por serie de Taylor", font=("Arial", 16, "bold"),
             bg=bg_color, fg=fg_color).grid(row=0, column=0, columnspan=2, pady=20)

    # Input grados
    tk.Label(frame, text="x (grados):", bg=bg_color, fg=fg_color).grid(row=1, column=0, sticky="e", padx=10, pady=10)
    x_entry = tk.Entry(frame, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg)
    x_entry.grid(row=1, column=1, padx=10, pady=10)

    # Input numero
    tk.Label(frame, text="Grados de aproximación (n):", bg=bg_color, fg=fg_color).grid(row=2, column=0, sticky="e", padx=10, pady=10)
    numero_entry = tk.Entry(frame, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg)
    numero_entry.grid(row=2, column=1, padx=10, pady=10)

    # Botón calcular
    tk.Button(frame, text="Calcular", command=calcular,
              bg=button_bg, fg=fg_color, activebackground="#777777").grid(row=3, column=0, columnspan=2, pady=20)

    root.mainloop()

# Función encargada de mostrar el resultado al usuario en una nueva ventana
# Recibe el resultado del cálculo, el valor original de x y el número de términos usados
def mostrar_resultado(resultado, x, numero):
    # Crea una nueva ventana usando tkinter
    result_window = tk.Tk()
    result_window.title("Resultado") # Título de la ventana
    # Dimensiones fijas de la ventana
    width, height = 800, 600
    # Obtiene las dimensiones de la pantalla del usuario
    screen_width = result_window.winfo_screenwidth()
    screen_height = result_window.winfo_screenheight()
    # Calcula la posición (x, y) para centrar la ventana en pantalla
    x_pos = int((screen_width - width) / 2)
    y_pos = int((screen_height - height) / 2)
    # Aplica el tamaño y posición calculada a la ventana
    result_window.geometry(f"{width}x{height}+{x_pos}+{y_pos}")
    # Bloquea el redimensionamiento manual de la ventana
    result_window.resizable(False, False)

    bg_color = "#2e2e2e"
    fg_color = "#ffffff"
    button_bg = "#555555"

    result_window.configure(bg=bg_color)

    # Frame centrado
    frame = tk.Frame(result_window, bg=bg_color)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    texto = f"sin({x}°) ≈ {resultado} usando {numero} términos de la serie de Taylor"
    tk.Label(frame, text=texto, font=("Arial", 14), bg=bg_color, fg=fg_color).pack(padx=20, pady=40)

    tk.Button(frame, text="Cerrar", command=result_window.destroy,
              bg=button_bg, fg=fg_color, activebackground="#777777").pack(pady=20)

    result_window.mainloop()
