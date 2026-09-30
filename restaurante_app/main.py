import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView

def main():
    servicio = RestauranteServicio()
    
    root = tk.Tk()
    app = LoginView(root, servicio)
    root.mainloop()

if __name__ == "__main__":
    main()