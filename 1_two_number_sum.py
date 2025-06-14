# O(N^2) time and O(1) space
def twoNumberSum(arr, targetSum):
    for i in range(0, len(arr)-1):
        firstNumber = arr[i]
        for j in range(i+1, len(arr)):
            secondNumber = arr[j]
            if firstNumber + secondNumber == targetSum:
                return [firstNumber, secondNumber]
    return []

# O(N) time | O(N) space
def twoNumberSumHash(arr, targetSum):
    map = {}
    for num in arr:
        if targetSum - num in map:
            return [num, targetSum-num]
        map[num] = True
    return []

# O(NlogN) time | O(1) space
def twoNumberSumTwoPointer(arr, targetSum):
    arr.sort()
    left, right = 0, len(arr)-1
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == targetSum:
            return [arr[left], arr[right]]
        elif currentSum < targetSum:
            left+=1
        else:
            right-=1
    return []




