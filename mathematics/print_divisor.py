import math

def printDivisor(n):

    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            print(i, end = " ")
            if n//i != i:
                print(n//i, end=" ")
    print()

printDivisor(17)
printDivisor(30)
printDivisor(36)