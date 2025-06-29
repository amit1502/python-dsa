def is_prime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i+=1
    return True

print(is_prime(17))
print(is_prime(27))
print(is_prime(29))