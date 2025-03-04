from Vehiculo import Vehiculo, Carro, Moto, Camion
from datetime import datetime
import time

class estacionamiento:
    def __init__(self):
        self.vehiculos = {}
        self.TARIFAS = {"moto": 1000, "carro": 2000, "camion": 5000}

    def registrar_vehiculo(self):
        tipo = input("Ingrese el tipo de vehículo (moto/carro/camion): ").lower()
        if tipo not in ["moto", "carro", "camion"]:
            print("Tipo de vehículo no válido.")
            return

        placa = input("Ingrese la placa del vehículo: ")
        marca = input("Ingrese la marca del vehículo: ")
        modelo = input("Ingrese el modelo del vehículo: ")
        hora_entrada = time.time()

        if tipo == "moto":
            vehiculo = Moto(placa, marca, modelo, hora_entrada)
        elif tipo == "carro":
            vehiculo = Carro(placa, marca, modelo, hora_entrada)
        else:
            vehiculo = Camion(placa, marca, modelo, hora_entrada)

        self.vehiculos[placa] = vehiculo
        print(f"Vehículo {placa} registrado exitosamente a las {datetime.fromtimestamp(hora_entrada).strftime('%H:%M')}")

    def registrar_salida(self):
        placa = input("Ingrese la placa del vehículo que sale: ")
        if placa not in self.vehiculos:
            print("El vehículo no está registrado en el estacionamiento.")
            return

        vehiculo = self.vehiculos.pop(placa)
        hora_salida = time.time()
        tiempo_estacionado = hora_salida - vehiculo.hora_entrada
        horas = int(tiempo_estacionado // 3600)
        minutos = int((tiempo_estacionado % 3600) // 60)
        
        if tiempo_estacionado < 3600:
            costo = vehiculo.tarifa
        else:
            costo = round((tiempo_estacionado / 3600) * vehiculo.tarifa, 2)

        print(f"Vehículo {placa} ha salido a las {datetime.fromtimestamp(hora_salida).strftime('%H:%M')}.")
        print(f"Tiempo estacionado: {horas} horas y {minutos} minutos. Tarifa a pagar: ${costo}")

    def ver_vehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos en el estacionamiento.")
            return

        print("Vehículos en el estacionamiento:")
        for vehiculo in self.vehiculos.values():
            print(f"Placa: {vehiculo.placa}, Tipo: {vehiculo.tipo}, Marca: {vehiculo.marca}, "
                  f"Modelo: {vehiculo.modelo}, Hora de entrada: {datetime.fromtimestamp(vehiculo.hora_entrada).strftime('%H:%M')}")
