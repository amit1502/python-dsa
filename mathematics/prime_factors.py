def primeFactors(n):
    if n <= 1:
        return

    i=2
    while i*i <= n:
        while n%i == 0:
            print(i, end = " ")
            n = n//i
        i+=1

    # important
    if n > 1:
        print(n, end = " ")

    print()

primeFactors(18)
primeFactors(8)
primeFactors(17)