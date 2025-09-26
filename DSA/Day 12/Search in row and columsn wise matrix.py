def binarysearch(arr,k):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==k:
            return True
        elif arr[mid]<k:
            low=mid+1
        else:
            high=mid-1
    return False
def searchinrowcol(matrix,target):
    n=len(matrix)
    m=len(matrix[0])
    for i in range(n):
        if binarysearch(matrix[i],target):
            return True
    return False
matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
result = searchinrowcol(matrix, 8)
print(result)