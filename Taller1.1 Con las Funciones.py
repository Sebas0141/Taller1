class Cuenta:
    
    def __init__(self, saldo_inicial):
        if saldo_inicial >= 0:
            self.saldo = saldo_inicial
        else:
            self.saldo = 0
            print("Error, Saldo inicial inválido. Se estableció el saldo en 0.")
    
    def credit(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("Error, el monto a depositar debe ser mayor que 0.")
    
    def cargar(self, monto):
        if monto > 0:
            if monto <= self.saldo:
                self.saldo -= monto
                print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
            else:
                print("El monto a cargar excede el saldo de la cuenta.")
        else:
            print("Error, el monto a cargar debe ser mayor que 0.")
    
    def obtener_saldo(self):
        return self.saldo

# Ejemplo de uso:
saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
mi_cuenta = Cuenta(saldo_inicial)

mi_cuenta.credit(100)  # Depositar 100
mi_cuenta.cargar(50)   # Retirar 50
print(f"Saldo actual: {mi_cuenta.obtener_saldo()}")