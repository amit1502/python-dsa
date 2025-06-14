def trailingZeroFactorial(num):
    ans = 0
    multiple_of_5 = 5

    while multiple_of_5 <= num:
        ans += (num // multiple_of_5)
        multiple_of_5 *= 5

    return ans

print(trailingZeroFactorial(4))
print(trailingZeroFactorial(5))
print(trailingZeroFactorial(10))
print(trailingZeroFactorial(100))