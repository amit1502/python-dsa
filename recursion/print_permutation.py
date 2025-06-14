def printPermutation(s, ans=""):
    if len(ans) == len(s):
        print(ans, end = " ")
        return
    for ch in s:
        if ch not in ans:
            ans += ch
            printPermutation(s, ans)
            ans = ans[:-1]


printPermutation("AB")
print()
printPermutation("ABC") 
print()
printPermutation("ABCD")