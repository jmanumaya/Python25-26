class CuentaCorriente:

    def __init__(self, dni, balance, name=""):
        self.dni = dni
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        res = False
        if amount <= self.balance:
            self.balance -= amount
            res = True
        return res
    
    def addAmount(self, amount):
        res = False
        if amount >= 0:
            self.balance += amount
            res = True
        return res
    
    def getDni(self):
        return self.dni
    
    def getBalance(self):
        return self.balance
            
    def __str__(self): 
        return f"Titular: {self.name}, with DNI: {self.dni}, have {self.balance}$"

    def __eq__(self, other): 
        return self.dni == other.getDni()

    def __lt__(self, other): 
        return self.balance < other.getBalance()
