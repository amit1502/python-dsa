def towerOfHanoi(n, n1="A", n2="B", n3="C"):

    if n == 0:
        return

    towerOfHanoi(n-1, n1, n3, n2)
    print(f"Move disk from {n1} to {n3}")
    towerOfHanoi(n-1, n2, n1, n3)


towerOfHanoi(1)
print("*"*20)
towerOfHanoi(2)
print("*"*20)
towerOfHanoi(3)
