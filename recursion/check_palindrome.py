def checkPalindromeRecursive(s, start, end):
    if start >= end:
        return True

    if s[start] != s[end]:
        return False

    return checkPalindromeRecursive(s, start+1, end-1)

def checkPalindrome(s):
    return checkPalindromeRecursive(s, 0 , len(s)-1)
    


print(checkPalindrome("abbcbba"))
print(checkPalindrome("geeks"))
