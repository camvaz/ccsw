import datetime

class Strats:
    
    def __init__(self):
        self.date = datetime.date.today()
        self.name = f"\n\t#  Codigo de metodos de prueba para el primer parcial de Control y Calidad de Software\n\n Fecha: {self.date} \tNombre: Victor Manuel Campos Vazquez"

    def prueba_1(self, stringToTest: str):
        return stringToTest.split(', ')
        

strat = Strats()

print(strat.prueba_1("Queen, 9, Metallica, 7, Doors, 8, Nirvana, 6"))