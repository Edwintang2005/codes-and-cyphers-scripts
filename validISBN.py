# For 10 digit isbns
import re

def getChecksum(isbn):
    sum = 0
    for i in range(len(isbn)):
        sum += (i + 1) * isbn[i]
    return sum

isbnInput = input("ISBN: ")
isbnInput = re.sub("[^0-9]", "", isbnInput)
if len(isbnInput) != 10:
    exit("This only works for 10 digit ISBNs")
isbn = [int(i) for i in isbnInput]
sum = getChecksum(isbn)
if ( sum % 11 == 0):
    print("Valid ISBN")
    exit()
print(f"invalid ISBN - {sum % 11}")

digit = int(input("Which digit does the error occur at: "))
for i in range(0, 10):
    isbn[digit - 1] = i
    if (getChecksum(isbn) % 11 == 0):
        print(f"Valid ISBN - {''.join(str(x) for x in isbn)} replacing {digit}th character with {i}")
        exit()
    else:
        print(f"testing {''.join(str(x) for x in isbn)}(digit {i}) - failed")
print("Unable to correct")