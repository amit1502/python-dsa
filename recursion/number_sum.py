def number_sum(n):
    if n == 0:
        return 0
    return number_sum(n-1) + n

print(number_sum(5))