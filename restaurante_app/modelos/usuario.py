class Usuario:
    def __init__(self, id_usuario, nombre, rol, clave):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.rol = rol
        self.clave = clave

    def to_dict(self):
        return {
            "id": self.id_usuario,
            "nombre": self.nombre,
            "rol": self.rol,
            "clave": self.clave
        }