from eulerFunction import getUnits
import math

mod = int(input("What mod are we working in? "))

units = getUnits(mod)
a = int(input("What element are we finding the order for? "))

if (a not in units):
    print(f"{a} is not a unit for mod {mod}!")
    exit()

i = 1
while 1:
    if (math.pow(a, i) % mod == 1):
        break
    else:
        i += 1
print(f"ord_({mod})({a}) = {i}")