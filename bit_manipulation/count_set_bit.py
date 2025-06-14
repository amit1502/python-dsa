def countSetBit(n):
    ans = 0
    while n:
        ans += 1
        n = (n & (n-1))

    return ans

print(countSetBit(10))
print(countSetBit(8))
print(countSetBit(12)) 