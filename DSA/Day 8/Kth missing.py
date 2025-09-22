def kth_missing(arr,k):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        missing=arr[mid]-(mid+1)
        if missing<k:
            low=mid+1
        else:
            high=mid-1
    return high+k+1
arr=[1,2,6]
k=3
s=kth_missing(arr,k)
print(s)
