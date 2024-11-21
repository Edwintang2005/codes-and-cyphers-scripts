# Algorithm to help decode an arithmetic encoding with 3 values
usingDefaultValues = input("Are you using default values (y/n)? ").lower()
firstChar = "s1"
secondChar = "s2"
thirdChar = "*"
if usingDefaultValues == "n":
    firstChar = input("First Character is: ")
    secondChar = input("Second Character is: ")
    thirdChar = input("Third Character is: ")

secondStart = float(input("Start of second character: "))
thirdStart = float(input("Start of third character: "))

encodeOrDecode = input("Are you encoding or decoding (E/D)? ").lower()
if encodeOrDecode == 'e':
    message = input("Input characters comma seperated: ").split(',')
    intStart = 0
    intEnd = 1
    for ch in message:
        if ch == firstChar:
            intEnd = intStart + (intEnd - intStart) * secondStart
        elif ch == secondChar:
            intEnd = intStart + (intEnd - intStart) * thirdStart
            intStart += (intEnd - intStart) * secondStart
        elif ch == thirdChar:
            intStart += (intEnd - intStart) * thirdStart
        else:
            exit("Improper message format")
    print(f"Choose a value in range {round(intStart, 4)} to {round(intEnd, 4)}")
else:
    value = float(input("Code value: "))
    intStart = 0
    intEnd = 1
    finalString = ""
    while True:
        diff = intEnd - intStart
        currPercent = (value - intStart)/(intEnd - intStart)
        if (currPercent < secondStart):
            finalString += firstChar
            print("1st Value")
            intEnd = intStart + diff * secondStart
        elif (currPercent < thirdStart):
            finalString += secondChar
            print("2nd Value")
            intEnd = intStart + diff * thirdStart
            intStart = intStart + diff * secondStart
        else:
            finalString += thirdChar
            print("3rd Value")
            break
    print(finalString)