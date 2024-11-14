from eulerFunction import getUnits
import math

def findInverse(mod, value):
    units = getUnits(mod)
    if value not in units:
        return 0
    for i in range(1,mod + 1):
        if (i * value % mod == 1):
            return i
    return 0


if __name__ == "__main__":
    mod = int(input("What mod are we working in? "))
    value = int(input("What value do you want to find inverse of? "))
    print(findInverse(mod, value))

