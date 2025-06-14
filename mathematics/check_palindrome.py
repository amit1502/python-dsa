def checkPalindrome(num):
    reverse, temp = 0, num
    while(temp):
        rem = temp%10
        reverse = reverse*10 + rem
        temp = temp//10
    return num == reverse

print(checkPalindrome(121))
print(checkPalindrome(123))