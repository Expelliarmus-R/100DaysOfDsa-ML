def totaldays(arr,c,m,k):
    n=len(arr)
    cnt=0
    noOfb=0
    for i in range(n):
        if arr[i]<=c:
            cnt+=1
        else:
            noOfb+=cnt//k
            cnt=0
    noOfb+=cnt/k
    return noOfb>=m
def garden(arr,m,k):
    n=len(arr)
    if m*k > n:
        return -1
    low=1
    high=max(arr)
    while low<=high:
        mid=(low+high)//2
        if totaldays(arr,mid,m,k):
            high=mid-1
        else:
            low=mid+1
    return low
arr=[7,7,7,7,13,11,12,7]
m=2
k=3
s=garden(arr,m,k)
print(s)
