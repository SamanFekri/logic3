__author__ = 'SKings'

from and3 import *
from or3 import *
from not3 import *

bits = [bit_3(1) for i in range(8)]
bits[2].setValue(-1)
myand = and3(bits[0],bits[1],bits[2])
print(myand.getResultBit().getValue())
print(myand.numOf1())

myor = or3(bits[0],bits[1],bits[2])
print(myor.getResultBit().getValue())
print(myor.numOf1())

mynot = not3(bits[0])
print(mynot.getResultBit().getValue())