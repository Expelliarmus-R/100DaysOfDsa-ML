def merge(arr,low,mid,high):
    cnt=0
    left=low
    right=mid+1
    temp=[]
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            cnt=(mid-left+1)
            right+=1
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]
    return cnt

def mergesort(arr,low,high):
    cnt=0
    if low>=high:
        return cnt
    mid=(low+high)//2
    cnt+=mergesort(arr,low,mid)
    cnt+=mergesort(arr,mid+1,high)
    cnt+=merge(arr,low,mid,high)
    return cnt

arr=[1,5,4,3,9,6]
inversions=mergesort(arr,0,len(arr)-1)
print(inversions)
