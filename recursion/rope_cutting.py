def ropeCutting(n, a, b, c):

    if n < 0:
        return -1

    if n == 0:
        return 0

    ans = max(ropeCutting(n-a, a, b, c), max(ropeCutting(n-b, a, b, c), ropeCutting(n-c, a, b, c)))

    if ans == -1:
        return -1

    return 1 + ans

print(ropeCutting(5, 2, 5, 1))
print(ropeCutting(23, 12, 9, 11))
print(ropeCutting(5, 4, 2, 6)) 