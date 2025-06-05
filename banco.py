class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depositados {cantidad}. Nuevo saldo: {self.__saldo}")

    def get_saldo_publico(self):
        return self.__saldo

mi_cuenta = CuentaBancaria(1000)
mi_cuenta.depositar(200)
print(mi_cuenta.__saldo)
