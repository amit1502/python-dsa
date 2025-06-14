# O(N) time | O(1) space
def validate_subsequence(arr, subsequence):
    i, j = 0, 0
    while i < len(arr) and j < len(subsequence):
        if arr[i] == subsequence[j]:
            j +=1
        i += 1
    if i >= len(arr):
        if j >= len(subsequence):
            return True
        return False
    else:
        return True
