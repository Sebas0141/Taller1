class Cuenta:
    
    saldo = 500
    
    def __init__(self, codigo, tipo):
        self.codigo = codigo
        self.tipo = tipo
    
    def val_saldo(self):
        if self.saldo >= 0:
            return True
        else:
            print("Error, Saldo inicial Inválido")
            return False
          
    def credit(self):
        if self.val_saldo():
            print(f"Cuenta Activa - Código: {self.codigo}, Tipo: {self.tipo}")
            opc = int(input("Digite 1: DEPOSITAR, 2: SACAR PLATA "))
            if opc == 1:
                dep = float(input("Ingrese el valor que desea depositar: "))
                self.saldo += dep
                print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
            elif opc == 2:
                sac = float(input("Ingrese el valor que desea sacar: "))
                if sac <= self.saldo:
                    self.saldo -= sac
                    print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
                else:
                    print("Fondos insuficientes")
            else:
                print("Operación no válida")
        else:
            print("Aplicación Inactiva")       
            
mi_cuenta = Cuenta(7474, "Ahorros")
mi_cuenta.credit()



            