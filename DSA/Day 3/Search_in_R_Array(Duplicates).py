def rotated(arr,k):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[low]==arr[mid]==arr[high]:
            low+=1
            high-=1
            continue
        if arr[mid]==k:
            return True
        elif arr[low]<=arr[mid]:
            if arr[low]<=k and k <= arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<=k and k <=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return False
arr=[4,4,5,5,0,1,2,3]
k=9
s=rotated(arr,k)
print(s)



