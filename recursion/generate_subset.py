def generateSubset(s, index, ans):
    if index >= len(s):
        print("subset: ", ans)
        return

    generateSubset(s, index+1, ans+s[index])
    generateSubset(s, index+1, ans)


generateSubset("AB", 0, "")
print("*"*20)
generateSubset("ABC", 0 , "")