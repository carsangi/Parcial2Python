import os
from Dominio.Inventario import Inventario
from Infraestructura.Persistencia import Persistencia

class Operacion:

    def vender(self):
        saver = Persistencia()
        inventario = Inventario()
        for file in os.listdir("./Files"):
            if '.json' in file:
                inventario.agregar_objeto(saver.load_json(file))






