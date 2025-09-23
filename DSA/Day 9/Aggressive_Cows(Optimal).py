def canpossible(arr,k,d):
    cows=1
    last=arr[0]
    n=len(arr)
    for i in range(1,n):
        if arr[i]-last>=d:
            cows+=1
            last=arr[i]
        if cows>=k:
            return True
    return False
def aggressivecows(arr,k):
    arr.sort()
    n=len(arr)
    low=arr[0]
    high=arr[n-1]
    while low <= high:
        mid=(low+high)//2
        if canpossible(arr,k,mid):
            low=mid+1
        else:
            high=mid-1
    return high
arr=[4,2,1,3,6]
k=2
print(aggressivecows(arr, k))
