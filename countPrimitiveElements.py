from eulerFunction import getEulerFunctionValue, getUnits
from findOrder import findOrder
import math

def myfilter(x, units, mod):
    order = findOrder(x, units, mod)
    return order != None and order == len(units)

def numberOfPrimitives(mod):
    øMod = getEulerFunctionValue(mod)
    øøMod = getEulerFunctionValue(øMod)
    return øøMod
def getPrimitives(mod):
    units = getUnits(mod)
    return list(filter(lambda x: myfilter(x, units, mod), units))


if __name__ == "__main__":
    mod = int(input("What mod are we working in? "))
    print(numberOfPrimitives(mod))
    doGetPrimitives = True if input("Continue and find Primitives(Y/N)? ").lower() == "y" else False
    if doGetPrimitives:
        print(getPrimitives(mod))
