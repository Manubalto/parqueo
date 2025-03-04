from Estacionamiento import estacionamiento
from Vehiculo import Vehiculo, Carro, Moto, Camion
from datetime import datetime
import time
class AProgram:
    def __init__(self):
        self.estacionamiento = estacionamiento()

    def menu(self):
        while True:
            print("\nMenú:")
            print("1. Registrar vehículo")
            print("2. Registrar salida")
            print("3. Ver vehículos")
            print("4. Salir")
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                self.estacionamiento.registrar_vehiculo()
            elif opcion == "2":
                self.estacionamiento.registrar_salida()
            elif opcion == "3":
                self.estacionamiento.ver_vehiculos()
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")
program = AProgram()
program.menu()

