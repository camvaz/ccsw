import datetime
from utils import Utils

class Strats:
    def __init__(self):
        self.date = datetime.date.today()
        self.name = f"\n\t#  Codigo de metodos de prueba para el primer parcial de Control y Calidad de Software\n\n'\
                     + Fecha: {self.date} \t Nombre: Victor Manuel Campos Vazquez"
        self.maxCharLength = 50

    def prueba_1(self, stringToTest: str):
        return stringToTest.split(', ')
    
    def prueba_2(self, stringToTest: str):
        return len(stringToTest.split(', ')) / 2
        
    def prueba_3(self, stringToTest: str):
        return len(stringToTest.split(', ')) / 2

    def prueba_4(self, stringToTest: str):
        return len(stringToTest.split(', ')) / 2

    def prueba_5(self, stringToTest: str):
        numbers = Utils.getIntsFromList(stringToTest.split(', ')) 
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
                              
    def prueba_7(self, stringToTest: str):
        numbers = Utils.getIntsFromList(stringToTest.split(', ')) 

        for i in numbers:
            for j in numbers:
                if i == j:
                    return False
        return True
    
    def prueba_8(self, stringToTest: str):
        values = stringToTest.split(', ')
        index = 0

        for i in values:
            try:
                int(i)
                if(index % 2 == 0):
                    return False
            except ValueError:
                pass
            index+=1

        return True
                              
    def prueba_9(self, stringToTest: str):
        values = stringToTest.split(', ')
        for val in values:
            for char in val:
                # Check for ascii values
                if (ord(char) >= 65 and ord(char) <= 90) or\
                    (ord(char) >= 97 and ord(char) <= 122) or\
                    (ord(char) >= 48 and ord(char) <= 57):
                    pass
                else:
                    return False
        return True
    
    def prueba_10(self, stringToTest: str):
        numbers = Utils.getIntsFromList(stringToTest.split(', '))
        for i in numbers:
            if i >= 10 or i <= 1:
                return False
        return True

    def prueba_11(self, stringToTest: str):
        numbers = Utils.getIntsFromList(stringToTest.split(', '))
        for i in numbers:
            if i <= 0:
                return False
        return True
    
    def prueba_12(self, stringToTest: str):
        numbers = Utils.getIntsFromList(stringToTest.split(', '))
        return len(numbers)

    def prueba_13(self, stringToTest: str):
        strings = Utils.getStringsFromList(stringToTest.split(', '))
        return len(strings)

    def prueba_14(self, stringToTest: str):
        strings = Utils.getStringsFromList(stringToTest.split(', '))
        return list(filter(lambda x: len(x) <= self.maxCharLength, strings)) == strings
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

# strat = Strats()
# print(strat.prueba_14('Queen, 10, Metallica, 8, Doors, 8, Nirvana, 7, Guns and Roses, 6, Caifanes, 5'))
