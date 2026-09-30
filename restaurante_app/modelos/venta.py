class Venta:
    def __init__(self, id_venta, cliente, total, productos):
        self.id_venta = id_venta
        self.cliente = cliente
        self.total = float(total)
        self.productos = productos  # Lista de diccionarios con los productos comprados

    def to_dict(self):
        return {
            "id": self.id_venta,
            "cliente": self.cliente,
            "total": self.total,
            "productos": self.productos
        }