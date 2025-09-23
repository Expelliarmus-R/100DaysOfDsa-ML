def canPossible(arr,k,d):
    n=len(arr)
    last=arr[0]
    cow=1
    for i in range(1,n):
        if arr[i]-last >= d:
            cow+=1
            last=arr[i]
        if cow>=k:
            return True
    return False
def aggressivecows(arr,k):
    n=len(arr)
    arr.sort()
    low=1
    high=arr[n-1]-arr[0]
    for i in range(low,high+1):
        if not canPossible(arr,k,i):
            return i-1
    return high
arr=[0,3,4,7,10,9]
k=4
print(aggressivecows(arr, k))


