class Astronauta:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def tarea(self):
        print(f"{self._nombre} es astronauta")
    
    def mostrarDatos(self):
        print("Nombre astronauta:",self._nombre)
        print("Edad astronauta:",self._edad)
        
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre= nombre
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 0 :
            self._edad = nueva_edad
        else:
            print("Edad Invalida")
    
    