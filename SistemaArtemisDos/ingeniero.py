from astronauta import Astronauta

class Ingeniero(Astronauta):
    def tarea(self):
        print(f"{self.get_nombre()} se encarga de los sistemas")