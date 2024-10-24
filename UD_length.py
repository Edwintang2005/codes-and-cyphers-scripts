from fractions import Fraction
import math


selectedMode = int(input(""" These are the modes available:
1. Trying to find r
2. Trying to find length from Kraft-McMillan coefficient
3. Trying to find missing length l
Which mode would you like to use? """))

if selectedMode == 1:
    lengths = input("Give series of codeword lengths: ")
    lengths = [int(x) for x in lengths.split(',')]
    result = 3
    radix = 1
    while result > 1:
        radix += 1
        num = 0
        for i in lengths:
            num += pow(radix, -i)
        result = num
    print(radix)
elif selectedMode == 2:
    radix = int(input("Give radix r: "))
    lengths = input("Give series of codeword lengths: ")
    lengths = [int(x) for x in lengths.split(',')]
    kraftCoefficient = Fraction(input("Give Kraft-McMillan coefficient K: "))
    for i in lengths:
        kraftCoefficient -= Fraction(1, pow(radix, i))
    print( math.log(kraftCoefficient, radix) * -1)
elif selectedMode == 3:
    lengths = input("Give series of codeword lengths: ")
    lengths = [int(x) for x in lengths.split(',')]
    radix = int(input("Give radix r: "))
    soFar = 0
    for i in lengths:
        soFar += Fraction(1, pow(radix, i))
    length = 2
    while True:
        if (soFar + Fraction(1, pow(radix, length)) <= 1):
            break
        length += 1
    print(length)