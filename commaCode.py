length = int(input("Input the length of your comma code: "))
codes = []
codeword = ""
for i in range(0, length + 1):
    if i == 0:
        codeword = "0"
    elif i == length:
        codeword = "1" * length
    else:
        codeword = "1" + codeword
    codes.append(codeword)
print(codes)
message = input("input the codeword numbering of the characters comma seperated (e.g. for a code s1s3s2 input 1,3,2): ").split(",")
messageInts = [int(x) for x in message]
codeword = ""
for i in messageInts:
    codeword = codeword + codes[i - 1]
print(codeword)