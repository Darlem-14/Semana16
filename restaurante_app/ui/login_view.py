import tkinter as tk
from tkinter import messagebox
from servicios.restaurante_servicio import RestauranteServicio
from ui.main_view import MainView

class LoginView:
    def __init__(self, root, servicio: RestauranteServicio):
        self.root = root
        self.root.title("Restaurante App - Login")
        self.root.geometry("400x300")
        self.root.config(bg="#f4f4f4")
        self.servicio = servicio

        # Título
        lbl_titulo = tk.Label(root, text="Sistema Restaurante", font=("Arial", 16, "bold"), bg="#f4f4f4")
        lbl_titulo.pack(pady=20)

        # Marco de formulario
        frame_form = tk.Frame(root, bg="#f4f4f4")
        frame_form.pack(pady=10)

        lbl_usuario = tk.Label(frame_form, text="Usuario:", font=("Arial", 11), bg="#f4f4f4")
        lbl_usuario.grid(row=0, column=0, sticky="w", pady=5)
        self.txt_usuario = tk.Entry(frame_form, font=("Arial", 11), width=20)
        self.txt_usuario.grid(row=0, column=1, pady=5)

        lbl_clave = tk.Label(frame_form, text="Contraseña:", font=("Arial", 11), bg="#f4f4f4")
        lbl_clave.grid(row=1, column=0, sticky="w", pady=5)
        self.txt_clave = tk.Entry(frame_form, font=("Arial", 11), width=20, show="*")
        self.txt_clave.grid(row=1, column=1, pady=5)

        # Botón Iniciar Sesión
        btn_login = tk.Button(root, text="Iniciar Sesión", font=("Arial", 11, "bold"), bg="#28a745", fg="white", width=15, command=self.verificar_login)
        btn_login.pack(pady=20)

    def verificar_login(self):
        nombre = self.txt_usuario.get()
        clave = self.txt_clave.get()

        usuario = self.servicio.validar_usuario(nombre, clave)
        if usuario:
            messagebox.showinfo("Éxito", f"¡Bienvenido, {usuario.nombre}!")
            self.root.destroy() # Cierra la ventana de login
            
            # Abre la ventana principal
            root_main = tk.Tk()
            MainView(root_main, self.servicio, usuario)
            root_main.mainloop()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")