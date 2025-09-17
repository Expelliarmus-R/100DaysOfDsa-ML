import sys

def minim(arr):
    n=len(arr)
    low=0
    high=n-1
    ans=sys.maxsize
    while low<=high:
        mid=(low+high)//2
        if arr[low]<=arr[high]:
            ans=min(ans,arr[low])
        if arr[low]<=arr[mid]:
            ans=min(ans,arr[low])
            low=mid+1
        else:
            ans=min(ans,arr[mid])
            high=mid-1
    return ans
arr=[4,5,0,1,2,3]
sol=minim(arr)
print(sol)
