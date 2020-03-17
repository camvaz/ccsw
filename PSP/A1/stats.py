import math
from LinkedList import LinkedList
from Node import Node

class Stats:
    def __init__(self, data: list):
        self.List: LinkedList = LinkedList() 
        for i in data:
            self.List.add(i)
    
    def mean(self):
        ref: Node = self.List.head
        sum: any = 0
        while(ref != None):
            sum += ref.data
            ref = ref.next

        return sum / self.List.length 
    
    def sumVariation(self):
        mean = self.mean()
        sum: any = 0
        ref: Node = self.List.head
        while(ref != None):
            sum += pow(ref.data-mean,2)
            ref = ref.next

        return sum

    def standardDeviation(self):
        return round(math.sqrt(self.sumVariation() / (self.List.length-1)),2)