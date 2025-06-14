def one_odd(arr):
    ans = 0
    for num in arr:
        ans = ans ^ num
    return ans

print(one_odd([4, 3, 4, 4, 4, 5, 5]))