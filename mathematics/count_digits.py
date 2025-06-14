def countDigits(num):
    count = 0
    while num:
        count+=1
        num = num//10

    return count

print(countDigits(100))