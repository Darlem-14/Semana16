import os
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    # Rutas absolutas dinámicas basadas en la ubicación de este archivo
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    RUTA_PRODUCTOS = os.path.join(BASE_DIR, "datos", "productos.json")
    RUTA_USUARIOS = os.path.join(BASE_DIR, "datos", "usuarios.json")
    RUTA_VENTAS = os.path.join(BASE_DIR, "datos", "ventas.json")

    def __init__(self):
        self.productos = self.cargar_productos()
        self.usuarios = self.cargar_usuarios()
        print("-> [DEBUG] Usuarios cargados:", [(u.nombre, u.clave) for u in self.usuarios])

    def cargar_productos(self):
        data = ArchivoServicio.leer_json(self.RUTA_PRODUCTOS)
        return [Producto(p["id"], p["nombre"], p["precio"], p["stock"]) for p in data]

    def cargar_usuarios(self):
        data = ArchivoServicio.leer_json(self.RUTA_USUARIOS)
        return [Usuario(u["id"], u["nombre"], u["rol"], u["clave"]) for u in data]
    def cargar_ventas(self):
        return ArchivoServicio.leer_json(self.RUTA_VENTAS)

    def validar_usuario(self, nombre, clave):
        nombre_ingresado = nombre.strip()
        clave_ingresada = str(clave).strip()

        for usuario in self.usuarios:
            if usuario.nombre.strip() == nombre_ingresado and str(usuario.clave).strip() == clave_ingresada:
                return usuario
        return None

    def registrar_venta(self, cliente, carrito):
        total = sum(item["precio"] * item["cantidad"] for item in carrito)
        ventas_actuales = ArchivoServicio.leer_json(self.RUTA_VENTAS)
        nuevo_id = len(ventas_actuales) + 1

        nueva_venta = Venta(nuevo_id, cliente, total, carrito)
        ventas_actuales.append(nueva_venta.to_dict())
        
        ArchivoServicio.escribir_json(self.RUTA_VENTAS, ventas_actuales)

        for item in carrito:
            for prod in self.productos:
                if prod.id_producto == item["id"]:
                    prod.stock -= item["cantidad"]
        
        self.guardar_productos()

    def guardar_productos(self):
        data = [p.to_dict() for p in self.productos]
        ArchivoServicio.escribir_json(self.RUTA_PRODUCTOS, data)