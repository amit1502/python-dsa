def power(x, n):

    if n == 0:
        return 1

    half_power = power(x, n//2)

    if n%2 != 0:
        return (half_power**2)*x

    return half_power**2


print(power(2, 10))
print(power(5, 3))
print(power(2, 5))