def checkKthBit(n, k):

    return n & (1 << (k-1)) > 0


print(checkKthBit(4, 3))
print(checkKthBit(4, 2))