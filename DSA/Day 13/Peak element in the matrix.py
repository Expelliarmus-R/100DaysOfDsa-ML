def maxele(arr,col):
    n=len(arr)
    maxi=0
    index=-1
    for i in range(n):
        if arr[i][col]>maxi:
            maxi=arr[i][col]
            index=i
    return index
def peak(arr):
    n=len(arr)
    m=len(arr[0])
    low=0
    high=m-1
    while low<=high:
        mid=(low+high)//2
        row=maxele(arr,mid)
        left=arr[row][mid-1] if mid-1>=0 else float('-inf')
        right=arr[row][mid+1] if mid+1<m else float('-inf')
        if arr[row][mid]>left and arr[row][mid]>right:
            return [row,mid]
        elif arr[row][mid]<left:
            high=mid-1
        else:
            low=mid+1
    return [-1,-1]


arr = [
    [0, 2, 5, 1, 4, 5],
    [2, 0, 3, 2, 3, 2],
    [1, 7, 6, 0, 1, 3],
    [3, 6, 2, 3, 7, 2]
]
print(peak(arr))
