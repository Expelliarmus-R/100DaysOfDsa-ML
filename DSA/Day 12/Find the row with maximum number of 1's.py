def lowerbound(arr,n,x):
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
def max1(matrix):
    n=len(matrix)
    m=len(matrix[0])
    cnt=0
    maxi=-1
    index=-1
    for i in range(n):
        cnt=m-lowerbound(matrix[i],m,1)
        if cnt>maxi:
            maxi=cnt
            index=i
    return index
matrix = [[0,0,1], [0, 1, 1], [0, 0, 0]]
n = 3
m = 3
print(max1(matrix))
