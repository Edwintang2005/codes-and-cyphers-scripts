import math

mod = int(input("To what modulo is your integer field? "))

units = []

for i in range(0, mod):
    if math.gcd(i, mod) == 1:
        units.append(i)
eulerFunction = len(units)
print(eulerFunction, units)

doEulersTheorem = True if input("Continue and do Euler's Theorem(Y/N)? ").lower() == "y" else False
if doEulersTheorem:
    number = int(input("For a^b, input a: "))
    power = int(input("For a^b, input b: "))
    # Euler's theorem tells us that given euler function = a, we know for x^y, x^a = 1 mod ____
    print(f"{number}^{power} mod {mod} = {math.pow(number, power % eulerFunction) % mod} mod {mod}!")