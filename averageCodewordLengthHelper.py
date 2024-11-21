from fractions import Fraction
import math

# shortcut tool FOR MARKOV SOURCES - Transition matrixes and equilibrium vectors
def markovSources():
    sourceLengths = []
    equilibriumVector = []
    # Collecting lengths for each source
    index = 0
    while True:
        inputStr = input(f"l{index + 1}: ")
        if inputStr == '':
            break
        sourceLengths.append(Fraction(inputStr))
        index += 1
    # Collecting equilibrium vector
    index = 0
    for i in sourceLengths:
        equilibriumVector.append(Fraction(input(f"Equilibirum vector position {index + 1}: ")))
        index += 1
    sum = 0
    # Finding dot product of the two vectors
    for i in range(0, len(sourceLengths)):
        sum += sourceLengths[i] * equilibriumVector[i]
    print(sum)

def shannonFanoCode():
    numCodes = int(input("How many codewords are there: "))
    radix = int(input("What radix is the code in: "))
    averageLength = Fraction()
    for i in range(0, numCodes):
        probability = Fraction(input(f"Input the probability for the {i + 1}th codeword: "))
        length = math.ceil(math.log(1/probability, radix))
        print(f"Length for this codeword is: {length}")
        averageLength += probability * length
    print(averageLength)

def extensionNtoInfShannon():
    numCodes = int(input("How many codewords are there: "))
    radix = int(input("What radix is the code in: "))
    averageLength = 0
    for i in range(0, numCodes):
        probability = Fraction(input(f"Input the probability for the {i + 1}th codeword: "))
        averageLength -= probability * math.log(probability, radix)
    print(averageLength)

if __name__ == "__main__":
    selectedMode = int(input(""" These are the modes available:
    1. Find length of Markov Source
    2. Find length of Shannon-Fano code
    3. Find average codeword length as n-> ∞ for the nth extension shannon-Fano code
    Which mode would you like to use? """))
    if selectedMode == 1:
        markovSources()
    elif selectedMode == 2:
        shannonFanoCode()
    elif selectedMode == 3:
        extensionNtoInfShannon()