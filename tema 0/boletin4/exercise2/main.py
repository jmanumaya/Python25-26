from empleado import Empleado
from directivo import Directivo
from oficial import Oficial
from operario import Operario
from tecnico import Tecnico

if __name__ == "__main__":
    e1 = Empleado("Rafa")
    d1 = Directivo("Mario")
    o1 = Operario("Alfonso")
    of1 = Oficial("Luis")
    t1 = Tecnico("Pablo")

    print(e1)
    print(d1)
    print(o1)
    print(of1)
    print(t1)