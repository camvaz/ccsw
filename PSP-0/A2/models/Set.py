class Set:
    data: list

    def __init__(self):
        super().__init__()

    def __init__(self, set: list):
        super().__init__()
        self.data = set
    
    def add(self, number: any) -> any:
        return self.data.append(number)

    def returnSet(self) -> dict:
        return DataFrame