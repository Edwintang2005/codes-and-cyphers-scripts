from eulerFunction import getUnits
import math

def findOrder(a, units, mod):
    if (a not in units):
        return
    i = 1
    while 1:
        if (math.pow(a, i) % mod == 1):
            break
        else:
            i += 1
    return i

if __name__ == "__main__":
    mod = int(input("What mod are we working in? "))

    units = getUnits(mod)
    a = int(input("What element are we finding the order for? "))
    i = findOrder(a, units, mod)
    if i != None:
        print(f"ord_({mod})({a}) = {i}")
    else:
        print(f"{a} is not a unit for mod {mod}!")