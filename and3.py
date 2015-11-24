__author__ = 'SKings'
from bit_3 import *;

class and3:
    def __init__(self,*bits):
        self.__resultBit = self.changeBits(*bits)


    def changeBits(self,*bits):
        self.__zeros = 0
        self.__mines1 = 0
        self.__bits = list(bits)
        for item in self.__bits:
            if(item.getValue() == -1):
                self.__mines1 += 1
            elif(item.getValue() == 0):
                self.__zeros += 1
        if(self.__mines1 > 0):
            return bit_3(-1)
        if (self.__zeros == 0):
            return bit_3(1)
        else:
            return bit_3(0)


    def numOf1(self):
        return (len(self.__bits) - self.__zeros - self.__mines1)

    def numOf0(self):
        return self.__zeros

    def numOfMines1(self):
        return self.__mines1

    def getResultBit(self):
        return self.__resultBit