__author__ = 'SKings'
class bit_3:
    def __init__(self,value):
        self.setValue(value)

    def setValue(self,value):
        if (value <= 1 and value >= -1):
            self.__value = value
        else :
            raise Exception

    def getValue(self):
        return self.__value