import tkinter as tk
from tkinter import messagebox, ttk
from servicios.restaurante_servicio import RestauranteServicio
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class MainView:
    def __init__(self, root, servicio: RestauranteServicio, usuario: Usuario):
        self.root = root
        self.root.title(f"Restaurante App - Menú Principal ({usuario.nombre})")
        self.root.geometry("600x450")
        self.servicio = servicio
        self.usuario = usuario
        self.carrito = []

        lbl_bienvenida = tk.Label(root, text=f"Bienvenido, {usuario.nombre} [Rol: {usuario.rol}]", font=("Arial", 14, "bold"))
        lbl_bienvenida.pack(pady=10)

        # Pestañas o secciones
        notebook = ttk.Notebook(root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Frame de Productos / Pedidos
        self.frame_pedidos = tk.Frame(notebook)
        notebook.add(self.frame_pedidos, text="Realizar Pedido")
        self.crear_interfaz_pedidos()

        # Frame de Admin (Solo si es administrador)
        if self.usuario.rol == "administrador":
            self.frame_admin = tk.Frame(notebook)
            notebook.add(self.frame_admin, text="Historial de Ventas")
            self.crear_interfaz_admin()

    def crear_interfaz_pedidos(self):
        lbl_prod = tk.Label(self.frame_pedidos, text="Productos Disponibles:", font=("Arial", 11, "bold"))
        lbl_prod.pack(anchor="w", padx=10, pady=5)

        # Tabla / Listado de productos
        self.tree_productos = ttk.Treeview(self.frame_pedidos, columns=("ID", "Nombre", "Precio", "Stock"), show="headings", height=6)
        self.tree_productos.heading("ID", text="ID")
        self.tree_productos.heading("Nombre", text="Nombre")
        self.tree_productos.heading("Precio", text="Precio")
        self.tree_productos.heading("Stock", text="Stock")
        self.tree_productos.pack(fill="x", padx=10)

        self.cargar_productos_tabla()

        # Controles de cantidad y compra
        frame_controles = tk.Frame(self.frame_pedidos)
        frame_controles.pack(pady=15)

        tk.Label(frame_controles, text="Cantidad:").grid(row=0, column=0, padx=5)
        self.txt_cantidad = tk.Entry(frame_controles, width=5)
        self.txt_cantidad.grid(row=0, column=1, padx=5)
        self.txt_cantidad.insert(0, "1")

        btn_agregar = tk.Button(frame_controles, text="Agregar al Pedido", bg="#007bff", fg="white", command=self.agregar_carrito)
        btn_agregar.grid(row=0, column=2, padx=10)

        btn_comprar = tk.Button(frame_controles, text="Finalizar Compra", bg="#28a745", fg="white", command=self.finalizar_compra)
        btn_comprar.grid(row=0, column=3, padx=10)

    def cargar_productos_tabla(self):
        for row in self.tree_productos.get_children():
            self.tree_productos.delete(row)
        for p in self.servicio.productos:
            self.tree_productos.insert("", "end", values=(p.id_producto, p.nombre, f"${p.precio:.2f}", p.stock))

    def agregar_carrito(self):
        seleccion = self.tree_productos.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un producto de la lista.")
            return
        
        item = self.tree_productos.item(seleccion)
        id_prod = item['values'][0]
        nombre_prod = item['values'][1]
        precio_prod = float(item['values'][2].replace("$", ""))
        stock_prod = int(item['values'][3])

        try:
            cantidad = int(self.txt_cantidad.get())
            if cantidad <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Error", "Ingresa una cantidad numérica válida.")
            return

        if cantidad > stock_prod:
            messagebox.showerror("Error", "No hay suficiente stock disponible.")
            return

        self.carrito.append({
            "id": id_prod,
            "nombre": nombre_prod,
            "precio": precio_prod,
            "cantidad": cantidad
        })
        messagebox.showinfo("Carrito", f"Se agregaron {cantidad}x {nombre_prod} al pedido.")

    def finalizar_compra(self):
        if not self.carrito:
            messagebox.showwarning("Advertencia", "El carrito está vacío.")
            return

        self.servicio.registrar_venta(self.usuario.nombre, self.carrito)
        messagebox.showinfo("Éxito", "¡Compra realizada con éxito!")
        self.carrito = []
        self.servicio.productos = self.servicio.cargar_productos()
        self.cargar_productos_tabla()

    def crear_interfaz_admin(self):
        lbl_ventas = tk.Label(self.frame_admin, text="Registro de Ventas Totales:", font=("Arial", 11, "bold"))
        lbl_ventas.pack(anchor="w", padx=10, pady=5)

        self.tree_ventas = ttk.Treeview(self.frame_admin, columns=("ID", "Cliente", "Total"), show="headings", height=10)
        self.tree_ventas.heading("ID", text="ID Venta")
        self.tree_ventas.heading("Cliente", text="Cliente")
        self.tree_ventas.heading("Total", text="Total ($)")
        self.tree_ventas.pack(fill="both", expand=True, padx=10, pady=10)

        btn_actualizar = tk.Button(self.frame_admin, text="Actualizar Lista", command=self.cargar_ventas_tabla)
        btn_actualizar.pack(pady=5)

        self.cargar_ventas_tabla()

    def cargar_ventas_tabla(self):
        for row in self.tree_ventas.get_children():
            self.tree_ventas.delete(row)
        
        ventas = ArchivoServicio.leer_json("datos/ventas.json")
        for v in ventas:
            self.tree_ventas.insert("", "end", values=(v["id"], v["cliente"], f"${v['total']:.2f}"))