from eulerFunction import getEulerFunctionValue, getUnits
from findOrder import findOrder
import math

def numberOfPrimitives(mod):
    øMod = getEulerFunctionValue(mod)
    øøMod = getEulerFunctionValue(øMod)
    return øøMod
def getPrimitives(mod):
    units = getUnits(mod)
    return list(filter(lambda x: (findOrder(x, units, mod) == len(units)), units))


if __name__ == "__main__":
    mod = int(input("What mod are we working in? "))
    print(numberOfPrimitives(mod))
    print(getPrimitives(mod))
