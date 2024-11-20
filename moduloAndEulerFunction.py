import math

def getUnits(mod):
    units = []

    for i in range(0, mod):
        if math.gcd(i, mod) == 1:
            units.append(i)
    return units

def getEulerFunctionValue(mod):
    units = getUnits(mod)
    return len(units)

def findOrder(a, units, mod):
    if (a not in units):
        return
    i = 1
    while 1:
        if (pow(a, i, mod) == 1):
            break
        else:
            i += 1
    return i

def findInverse(mod, value):
    units = getUnits(mod)
    if value not in units:
        return 0
    for i in range(1,mod + 1):
        if (i * value % mod == 1):
            return i
    return 0

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

def eulerFunction():
    mod = int(input("To what modulo is your integer field? "))
    eulerFunction = getEulerFunctionValue(mod)
    print(eulerFunction)

    doEulersTheorem = True if input("Continue and do Euler's Theorem(Y/N)? ").lower() == "y" else False
    if doEulersTheorem:
        number = int(input("For a^b, input a: "))
        power = int(input("For a^b, input b: "))
        # Euler's theorem tells us that given euler function = a, we know for x^y, x^a = 1 mod ____
        print(f"{number}^{power} mod {mod} = {pow(number, power % eulerFunction, mod)} mod {mod}!")

def findOrderMain():
    mod = int(input("What mod are we working in? "))

    units = getUnits(mod)
    a = int(input("What element are we finding the order for? "))
    i = findOrder(a, units, mod)
    if i != None:
        print(f"ord_({mod})({a}) = {i}")
    else:
        print(f"{a} is not a unit for mod {mod}!")

def findInverseMain():
    mod = int(input("What mod are we working in? "))
    value = int(input("What value do you want to find inverse of? "))
    print(findInverse(mod, value))

def findPrimitives():
    mod = int(input("What mod are we working in? "))
    print(numberOfPrimitives(mod))
    doGetPrimitives = True if input("Continue and find Primitives(Y/N)? ").lower() == "y" else False
    if doGetPrimitives:
        print(getPrimitives(mod))

if __name__ == "__main__":
    choice = int(input("""
    Input which euler function related functionality you wish to use:
    1. Evaluate the euler function value for a modulo, and do Euler's Theorem
    2. Determine the order of a element in a certain modulo field
    3. Find the inverse of an element in a modulo field
    4. FInd the primitives in a modulo field
Please type the number here: """))
    print()
    if choice == 1:
        eulerFunction()
    elif choice == 2:
        findOrderMain()
    elif choice == 3:
        findInverseMain()
    elif choice == 4:
        findPrimitives()