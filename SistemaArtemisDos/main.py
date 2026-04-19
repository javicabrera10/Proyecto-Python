from piloto import Piloto
from ingeniero import Ingeniero
from cientifico import Cientifico
from nave import Nave
from mision import Mision
from fotografo import Fotografo


# Crear nave
nave = Nave("Orion", "Tripulada", 4)

# Crear misión
mision = Mision("Artemis II", "Luna", 10, nave)

# Crear astronautas (distintos tipos)
astronauta1 = Piloto("Juan", 40)
astronauta2 = Ingeniero("Ana", 38)
astronauta3 = Cientifico("Luis", 45)
astronauta4 = Fotografo("Marcelo",20)

# Agregar a la misión
mision.agregar_astronauta(astronauta1)
mision.agregar_astronauta(astronauta2)
mision.agregar_astronauta(astronauta3)
mision.agregar_astronauta(astronauta4)

# Iniciar misión
mision.iniciar_mision()

astronauta1.mostrarDatos()
astronauta1.edad = 24 #se setea la edad no lleva ()
astronauta1.mostrarDatos()
mision.finalizar_mision()