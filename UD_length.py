print("""
1. Trying to find r
2. Trying to find length
""")

selectedMode = 1

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