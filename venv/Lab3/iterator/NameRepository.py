from Lab3.iterator.Container import Container
from Lab3.iterator.Iterator import Iterator


class NameRepository():
    names = ["Robert", "John", "Julie", "Lora"]
    
    def __iter__(self):
        self.__index = 0
        return self
    
    def __next__(self):
        if self.__index >= len(self.names):
            raise StopIteration
        elem = self.names[self.__index]
        self.__index += 1
        return elem

    '''def iterator(self):
        return NameIterator()
    
    class _NameIterator(Iterator):
        index = 0
        def has_next(self):
            if(index < names.lenght()):
                return True
            else:
                return False
        
        def next(self):
            if (self.has_next()):
                self.index = self.index + 1
                return names[self.index]
            else:
                return None
        '''