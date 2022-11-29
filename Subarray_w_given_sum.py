def subArraySum(arr:list[int], n:int, s:int):
    currentSum = arr[0]
    start = 0
    i = 1
    while i <= n:
        while (currentSum > s and start<i-1):
            currentSum -= arr[start]
            start += 1
        if currentSum == s:
            return [start, i-1] if start != i-1 else [start]
        if i < n:
            currentSum += arr[i]
        i += 1
    return [-1]
if __name__ == "__main__":
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    n = len(arr)
    sum = 10
    arr1 = subArraySum(arr, n, sum)
    print(arr1)


