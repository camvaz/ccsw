# Importamos DataFrame para recibit lecturas de pandas
from pandas import DataFrame

class Set:
    def __init__(self, set: list = []):
        # Constructor que recibe una lista de manera opcional
        super().__init__()
        self.data = set
    
    def add(self, number):
        # Agregamos info de esta lista por medio de Append 
        return self.data.append(number)

    def returnSet(self) -> DataFrame:
        # Una vez almacenados retornamos la lista por medio de un DataFrame
        return DataFrame({"data": self.data})