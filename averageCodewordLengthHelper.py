from fractions import Fraction

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

markovSources()