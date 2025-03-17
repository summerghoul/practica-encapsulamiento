class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = saldo_inicial

    # setter (configurar o editar)
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"se han depositado ${cantidad} exitosamente")
        else:
            print("ERROR: cantidad ingresada invalida ")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se han retirado exitosamente ${cantidad}")
        else:
            print("ERROR: saldo insuficiente o cantidad invalida")

    # getter (obtener informacion privada a travéz de un metodo publico)

    def obtener_saldo(self):
        print(f"Su saldo es de ${self.__saldo}")
