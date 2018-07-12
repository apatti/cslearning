

class stack:
    
    def __init__(self):
        self.__items=[]

    def push(self,elem):
        self.__items.append(elem)

    def pop(self):
        return self.__items.pop()

    def isEmpty(self):
        return self.__items==[]

    def size(self):
        return len(self.__items)

    def peek(self):
        return self.__items[len(self.__items)-1]

