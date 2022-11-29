'''
Given an array of integers of size n, Our aim is to calculate the maximum sum of k consecutive elements in the array.
Input  : arr[] = {100, 200, 300, 400}, k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4 
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.

Input  : arr[] = {2, 3}, k = 3
Output : Invalid
'''
import sys
MIN_INT = -sys.maxsize
def max_sum1(arr:list[int], n:int, k:int):
    max_sum = MIN_INT
    for i in range(n-k + 1):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i+j]
        max_sum = max(max_sum, current_sum)
    return max_sum
def max_sum2(arr:list[int], n:int, k:int):
    if n < k:
        return -1
    max_sum = 0
    for i in range(k):
        max_sum += arr[i]
    window_sum = max_sum
    for i in range(k,n):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(window_sum, max_sum)
    return max_sum
if __name__ == '__main__':
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    n = len(arr)
    result = max_sum2(arr, n, k)
    print(result)