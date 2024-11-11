import math

def fermatFactorise(n):
    found = False
    # Fermats only works for odd positive integers!
    # Checking odd
    if n <= 0:
        return [n]
    # Checking even
    if n % 2 == 0:
        return[n/2, 2]
    
    a = math.ceil(math.sqrt(n))
    if (math.pow(a, 2) == n):
        return [a, a]
    while not found:
        newN = math.pow(a, 2) - n
        b = int(math.sqrt(newN))
        if (math.pow(b, 2) == newN):
            found = True
        else:
            a = a + 1
    return [a - b, a + b]
    

number = int(input("Input the number you want to factorise is: "))
factorisation = fermatFactorise(number)
print(factorisation)
print("b - a is equal to: " +  str(abs(factorisation[1] - factorisation[0])))
