# For 10 digit isbns
import re

input = input("ISBN: ")
input = re.sub("[^0-9]", "", input)
if len(input) != 10:
    exit("Invalid ISBN")
isbn = [int(i) for i in input]
sum = 0
for i in range(len(isbn)):
    sum += (i + 1) * isbn[i]
if (sum % 11 == 0):
    print("Valid ISBN")
else:
    print(f"invalid ISBN - {sum % 11}")