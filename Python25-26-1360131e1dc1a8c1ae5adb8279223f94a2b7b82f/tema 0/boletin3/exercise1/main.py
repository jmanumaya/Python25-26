from cuentaCorriente import CuentaCorriente

def main():
    cc1 = CuentaCorriente("12345678P", 1000)
    cc2 = CuentaCorriente("23456789P", 1000, "Pepe")

    print(cc1)
    print(cc2)

    print("Success Operation") if cc2.withdraw(int(input("Please enter a amount withdraw: "))) else print("Operation Error")
    print("Success Operation") if cc1.addAmount(int(input("Please enter a amount to add: "))) else print("Operation Error")

    print(cc1)
    print(cc2)
    print(cc1.__eq__(cc2))
    print(cc2.__lt__(cc1))
main()