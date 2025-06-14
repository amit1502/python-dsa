def sieve(n):

    arr = [True for i in range(n+1)]

    arr[0], arr[1] = False, False

    for i in range(2, n+1):
        if arr[i] is True:
            print(i, end=" ")
            for j in range(i*i, n+1, i):
                arr[j] = False

    print()

sieve(10)
sieve(50)
sieve(100)