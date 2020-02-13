import datetime

class Strats:
    def __init__(self):
        self.date = datetime.date.today()
        self.name = f"\n\t#  Codigo de metodos de prueba para el primer parcial de Control y Calidad de Software\n\n'\
                     + Fecha: {self.date} \t Nombre: Victor Manuel Campos Vazquez"

    def prueba_1(self, stringToTest: str):
        return stringToTest.split(', ')
    
    def prueba_2(self, stringToTest: str):
        return len(stringToTest.split(', ')) / 2
        
    def prueba_3(self, stringToTest: str):
        return len(stringToTest.split(', ')) / 2

    def prueba_4(self, stringToTest: str):
        return len(stringToTest.split(', ')) / 2

    def prueba_5(self, stringToTest: str):
        values = stringToTest.split(', ')
        numbers = []

        # Obtenemos datos int:
        for i in values:
            try:
                numbers.append(int(i))
            except ValueError:
                pass

        sortedList = numbers[:]
        sortedList.sort(reverse=True)
        
        # Comparamos original con ordenada
        return sortedList == numbers

    def prueba_6(self, stringToTest: str):
        values = stringToTest.split(', ')
        index = 0

        # Revisa que sean convertibles a int,
        # si lo son y el indice es par retorna false
        for i in values:
            try:
                int(i)
                if(index % 2 == 0):
                    return False
                
            except ValueError:
                pass
            
            index+=1

        return True
                              
                              
                              

    #=== PLAYGROUND


    # def prueba_3(self, stringToTest: str):
    #     return
    # def prueba_3(self, stringToTest: str):
    #     return
    # def prueba_3(self, stringToTest: str):
    #     return
    # def prueba_3(self, stringToTest: str):
    #     return
    # def prueba_3(self, stringToTest: str):
    #     return
    # def prueba_3(self, stringToTest: str):
    #     return
    # def prueba_3(self, stringToTest: str):
    #     return
    # def prueba_3(self, stringToTest: str):
    #     return
    # def prueba_3(self, stringToTest: str):
    #     return
    # def prueba_3(self, stringToTest: str):
    #     return
    # def prueba_3(self, stringToTest: str):
    #     return
    # def prueba_3(self, stringToTest: str):
    #     return
    # def prueba_3(self, stringToTest: str):
    #     return
    # def prueba_3(self, stringToTest: str):
    #     return

# strat = Strats()
# print(strat.prueba_5('Queen, 10, Metallica, 8, Doors, 8, Nirvana, 7, Guns and Roses, 6, Caifanes, 5'))
