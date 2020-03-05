import math

class Stats:
    x: list

    def __init__(self, data: list):
        self.x = data
    
    def mean(self):
        return sum(self.x) / len(self.x)
    
    def sumVariation(self):
        mean = self.mean()
        return sum([pow(i - mean,2) for i in self.x])

    def standardDeviation(self):
        return math.sqrt(self.sumVariation() / (len(self.x) - 1))