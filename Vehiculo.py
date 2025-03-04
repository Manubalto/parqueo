from datetime import datetime
import time
class Vehiculo:
         def __init__(self, placa, marca, modelo, hora_entrada):
            self.placa = placa
            self.marca = marca
            self.modelo = modelo
            self.hora_entrada = hora_entrada

class Carro(Vehiculo):
        def __init__(self, placa, marca, modelo, hora_entrada):
            super().__init__(placa, marca, modelo, hora_entrada)
            self.tarifa = 2000
            self.tipo = "carro"

class Moto(Vehiculo):
        def __init__(self, placa, marca, modelo, hora_entrada):
            super().__init__(placa, marca, modelo, hora_entrada)
            self.tarifa = 1000
            self.tipo = "moto"

class Camion(Vehiculo):
        def __init__(self, placa, marca, modelo, hora_entrada):
            super().__init__(placa, marca, modelo, hora_entrada)
            self.tarifa = 5000
            self.tipo = "camion"

      
        
   