from astronauta import Astronauta

class Cientifico(Astronauta):
    def tarea(self):
        print(f"{self.get_nombre()} realiza experimentos")