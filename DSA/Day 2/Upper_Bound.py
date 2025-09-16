def lower_bound(arr,x):
    n=len(arr)
    ans=n
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=x:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
arr=[1,2,3,5]
x=4
ans=lower_bound(arr,x)
print(ans)