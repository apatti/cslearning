
class Queue:
    
    def __init__(self):
        self.__items=[]

    def enqueue(self,item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0)
        
    def size(self):
        return len(self.__items)

    def peek(self):
        return self.__items[0]

    def isEmpty():
        return self.__items == []
