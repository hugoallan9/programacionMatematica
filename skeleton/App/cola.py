class Quee():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def quee(self, item):
        self.items.append(item)
        
            
    def dequee(self):
        return self.items.pop(0)

    
    def peek(self):
        if ( self.items.isEmpty() ):
            print 'La cola esta vacia'
        else: 
            return self.items[0]
