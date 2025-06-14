def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a%b)

print(gcd(12, 8))
print(gcd(8, 12))
print(gcd(7, 9))