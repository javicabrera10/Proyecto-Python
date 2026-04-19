from astronauta import Astronauta

class Fotografo(Astronauta):
    def tarea(self):
        print(f"{self.get_nombre()} saca fotos por todos lados...")