import math
from fractions import Fraction

base = int(input("What n-ary is the code in? "))
colCount = int(input("How Many Columns? "))
decPlace = int(input("How Many Decimal Places? "))
totalEntropy = 0
for i in range(1, colCount + 1):
    transitionMatrixValues = input(f"Give Transition Matrix Values in Column {i} (Comma seperated): ").split(',')
    transitionMatrixValues = list(map(lambda x: float(x), transitionMatrixValues))
    equilibriumValue = Fraction(input(f"Give equilibrium value for column {i}: "))
    columnEntropy = 0
    for val in transitionMatrixValues:
        columnEntropy -= val * math.log(val, base)
    print(f"    The column entropy for column {i} = {round(columnEntropy, decPlace)}")
    totalEntropy += columnEntropy * equilibriumValue
print(f"    Total Markov Entropy is: {round(totalEntropy, decPlace)}")