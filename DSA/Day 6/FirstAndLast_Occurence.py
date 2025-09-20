def first(arr,target):
    n=len(arr)
    low=0
    high=n-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
def last(arr,target):
    n = len(arr)
    low = 0
    high = n - 1
    ans = -1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans-1
def count(arr,target):
    f=first(arr,target)
    l=last(arr,target)
    return [f,l]
arr=[1,2,3,4,4,5]
target=4
s=count(arr,target)
print(s)


