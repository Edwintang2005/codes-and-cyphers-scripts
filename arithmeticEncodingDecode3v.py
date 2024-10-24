# Algorithm to help decode an arithmetic encoding with 3 values
firstChar = input("First Character is: ")
secondChar = input("Second Character is: ")
thirdChar = input("Third Character is: ")

secondStart = float(input("Start of second character: "))
thirdStart = float(input("Start of third character: "))
value = float(input("Code value: "))
intStart = 0
intEnd = 1
finalString = ""
while True:
    currPercent = (value - intStart)/(intEnd - intStart)
    if (currPercent < secondStart):
        finalString += firstChar
        print("1st Value")
        diff = intEnd - intStart
        intEnd = intStart + diff * secondStart
    elif (currPercent < thirdStart):
        finalString += secondChar
        print("2nd Value")
        diff = intEnd - intStart
        intEnd = intStart + diff * thirdStart
        intStart = intStart + diff * secondStart
        
    else:
        finalString += thirdChar
        print("3rd Value")
        break
print(finalString)