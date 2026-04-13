class Nave:
    def __init__(self, nombre, tipo, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad

    def despegar(self):
        print(f"La nave {self.nombre} está despegando...")
    def aterrizar(self):
        print(f"Aterrizando {self.nombre}")