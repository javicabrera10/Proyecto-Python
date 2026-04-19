from astronauta import Astronauta

class Piloto(Astronauta):
    def tarea(self):
        print(f"{self.get_nombre()} es el piloto de la misión")
    
