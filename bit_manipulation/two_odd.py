def two_odd(arr):
    xor = 0
    for num in arr:
        xor = xor ^ num

    partition = (xor & ~(xor-1))

    res1, res2 = 0, 0

    for num in arr:
        if num & partition > 0:
            res1 = res1 ^ num
        else:
            res2 = res2 ^ num

    print(res1, res2)


two_odd([3, 4, 3, 4, 5, 4, 4, 6, 7, 7])
two_odd([3, 4, 3, 4, 5, 4, 4, 6, 6 , 7])
