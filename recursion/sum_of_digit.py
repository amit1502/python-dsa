def sumOfDigit(n):
    if n == 0:
        return 0

    return (n%10) + sumOfDigit(n//10)


print(sumOfDigit(111))
print(sumOfDigit(5))
print(sumOfDigit(99))