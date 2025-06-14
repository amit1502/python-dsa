def subsetSumProblem(arr, targetSum, index=0):
    if index >= len(arr):
        if targetSum == 0:
            return 1
        return 0

    return subsetSumProblem(arr, targetSum-arr[index], index+1) + \
           subsetSumProblem(arr, targetSum, index+1)


print(subsetSumProblem([10,5,2,3,6], 8))
print(subsetSumProblem([1,2,3], 4))
print(subsetSumProblem([10,20,15], 37))
print(subsetSumProblem([10,20,15], 0))