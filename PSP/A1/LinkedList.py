from A1.Node import Node

class LinkedList:
    def __init__(self):
        super().__init__()
        self.head: Node = None 
        self.length: int = 0

    def add(self, data: any):
        if(self.head):
            ref: Node = self.head
            while(ref.next != None):
                ref = ref.next
            ref.next = Node(data) 
        else:
            self.head = Node(data) 
        
        self.length += 1
        return self.length

    def print(self):
        ref: Node = self.head
        while(ref != None):
            print(ref.data)    
            ref = ref.next