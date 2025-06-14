def sortedSquaredArray(arr):
    ans = []
    left, right = 0, len(arr)-1
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            ans.insert(0, arr[left]**2)
            left+=1
        else:
            ans.insert(0, arr[right]**2)
            right-=1
    return ans



print(sortedSquaredArray([-7, -5, -4, 3, 6, 8, 9]))