def search_insert(arr,x):
    n=len(arr)
    ans=n
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[1,2,5,9]
x=3
ans=search_insert(arr,x)
print(ans)