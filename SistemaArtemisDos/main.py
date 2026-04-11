from piloto import Piloto
from ingeniero import Ingeniero
from cientifico import Cientifico
from nave import Nave
from mision import Mision

# Crear nave
nave = Nave("Orion", "Tripulada", 4)

# Crear misión
mision = Mision("Artemis II", "Luna", 10, nave)

# Crear astronautas (distintos tipos)
astronauta1 = Piloto("Juan", 40)
astronauta2 = Ingeniero("Ana", 38)
astronauta3 = Cientifico("Luis", 45)

# Agregar a la misión
mision.agregar_astronauta(astronauta1)
mision.agregar_astronauta(astronauta2)
mision.agregar_astronauta(astronauta3)

# Iniciar misión
mision.iniciar_mision()