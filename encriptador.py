import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# Generar clave
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as clave_archivo:
        clave_archivo.write(clave)
    messagebox.showinfo("Clave generada", "La clave ha sido generada y guardada en 'clave.key'.")

# Cargar clave
def cargar_clave():
    return open("clave.key", "rb").read()

# Encriptar mensaje
def encriptar_mensaje():
    mensaje = mensaje_input.get()
    clave = cargar_clave()
    fernet = Fernet(clave)
    mensaje_encriptado = fernet.encrypt(mensaje.encode())
    resultado_output.delete(0, tk.END)
    resultado_output.insert(0, mensaje_encriptado.decode())

# Desencriptar mensaje
def desencriptar_mensaje():
    mensaje_encriptado = mensaje_input.get()
    clave = cargar_clave()
    fernet = Fernet(clave)
    try:
        mensaje_desencriptado = fernet.decrypt(mensaje_encriptado.encode()).decode()
        resultado_output.delete(0, tk.END)
        resultado_output.insert(0, mensaje_desencriptado)
    except Exception as e:
        messagebox.showerror("Error", "No se pudo desencriptar el mensaje.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Encriptador de Mensajes")

# Widgets
tk.Label(ventana, text="Mensaje:").grid(row=0, column=0, padx=10, pady=10)
mensaje_input = tk.Entry(ventana, width=50)
mensaje_input.grid(row=0, column=1, padx=10, pady=10)

tk.Button(ventana, text="Generar Clave", command=generar_clave).grid(row=1, column=0, columnspan=2, padx=10, pady=5)
tk.Button(ventana, text="Encriptar", command=encriptar_mensaje).grid(row=2, column=0, columnspan=2, padx=10, pady=5)
tk.Button(ventana, text="Desencriptar", command=desencriptar_mensaje).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

tk.Label(ventana, text="Resultado:").grid(row=4, column=0, padx=10, pady=10)
resultado_output = tk.Entry(ventana, width=50)
resultado_output.grid(row=4, column=1, padx=10, pady=10)

# Iniciar la ventana principal
ventana.mainloop()