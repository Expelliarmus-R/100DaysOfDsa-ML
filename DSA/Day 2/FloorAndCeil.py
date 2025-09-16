def floor(arr,x):
    n=len(arr)
    low=0
    high=n-1
    ans=-1
    while low <= high:
        mid=(low+high)//2
        if arr[mid]<=x:
            ans=arr[mid]
            low = mid + 1
        else:
            high = mid - 1
    return ans

def ceil(arr,x):
    n=len(arr)
    low=0
    high=n-1
    ans=-1
    while low <= high :
        mid=(low+high)//2
        if arr[mid]>=x:
            ans=arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ans

arr=[1,2,3,5,6,7,8]
x=4
s1=floor(arr,x)
s2=ceil(arr,x)
print(s1,s2)
