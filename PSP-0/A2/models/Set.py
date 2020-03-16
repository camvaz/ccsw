from pandas import DataFrame

class Set:
    data: list

    def __init__(self, set: list = []):
        super().__init__()
        self.data = set
    
    def add(self, number):
        return self.data.append(number)

    def returnSet(self) -> DataFrame:
        return DataFrame({"data": self.data})