import math

def checkPseudoprime(n, base):
    # Check gcd(base, n) == 1 which is equivalent to checking base^{n-1} == 1 mod n
    return pow(base, n-1, n) == 1

number = int(input("Enter the number n: "))
bases = input("Enter the list of bases (comma seperated): ").split(',')
truthValues = list(map(lambda base : checkPseudoprime(number, int(base)), bases))
print(list(map(lambda x, y: (x,y), bases, truthValues)))
