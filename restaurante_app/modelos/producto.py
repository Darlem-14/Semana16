class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = int(stock)

    def to_dict(self):
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }