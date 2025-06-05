class Vehiculo:
    def __init__(self, id_vehiculo):
        self.id = id_vehiculo
        print(f"Vehículo ID {self.id} creado.")

class Coche(Vehiculo):
    def __init__(self, marca, modelo): # ¡ERROR AQUÍ! Falta llamar a super().__init__()
        self.marca = marca
        self.modelo = modelo
        print(f"Coche {self.marca} {self.modelo} inicializado.")

    def mostrar_detalles(self):
        # Intenta acceder a self.id, que debería ser inicializado por Vehiculo.__init__
        return f"{self.marca} {self.modelo} (ID: {self.id})"

c = Coche("Ford", "Fiesta")
print(c.mostrar_detalles())
