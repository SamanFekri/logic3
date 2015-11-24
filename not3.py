__author__ = 'SKings'
from bit_3 import *
class not3:
    def __init__(self,bit):
        self.__resultBit = self.changeBits(bit)


    def changeBits(self,bit):
        if(bit.getValue() == -1):
            return bit_3(1)
        elif(bit.getValue() == 1):
            return bit_3(-1)
        else:
            return bit_3(0)

    def getResultBit(self):
        return self.__resultBit