class Mision:
    def __init__(self, nombre, destino, duracion, nave):
        self.nombre = nombre
        self.destino = destino
        self.duracion = duracion
        self.nave = nave
        self.tripulacion = []

    def agregar_astronauta(self, astronauta):
        self.tripulacion.append(astronauta)

    def iniciar_mision(self):
        print(f"Iniciando misión {self.nombre} hacia {self.destino}")
        
        self.nave.despegar()

        print("Tripulación en acción:")
        for a in self.tripulacion:
            a.tarea()   # POLIMORFISMO