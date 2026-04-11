from astronauta import Astronauta

class Piloto(Astronauta):
    def tarea(self):
        print(f"{self.nombre} es el piloto de la misión")