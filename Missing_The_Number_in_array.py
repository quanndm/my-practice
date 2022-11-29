
def findMissing1(arr:list[int], n:int):
    '''
        finding missing number in array using hash
        - Create a new temp array with "n + 1" size
        - Traverse the input array arr[], and do following for each arr[i] => temp[arr[i]-1] = 1 
        - Traverse temp[] , if element in temp array is 0, it is the missing number
        - time complexity: O(N)
        - Auxiliary space: O(N)
    '''
    temp = [0] * (n+1)
    ans = -1
    for i in range(n):
        temp[arr[i] - 1] = 1
    for i in range(n+1):
        if temp[i] == 0:
            ans = i + 1
    return ans

def findMissing2(arr:list[int], n:int):
    '''
        Finding missing number in array using (summation of first N natural numbers)
        - Calculate the sum of the first N natural numbers as sumtotal= N*(N+1)/2.
        - Find the sum of all the array elements.
        - Missing number =  SumTotal – sum of array
        - time complexity: O(N)
        - Auxiliary space: O(1)
        ### Disadvantages 
        - Maybe overflow if N is large. 
    '''
    sum_total = (n+1)*(n+2)/2
    sum_array = sum(arr)
    return int(sum_total - sum_array)

if __name__ == '__main__':
    arr = [1, 2, 3, 5]
    n = len(arr)
    res = findMissing2(arr, n)
    print(res)
