def count(arr,threshold):
    sumofboards=0
    painter=1
    n=len(arr)
    for i in range(n):
        if sumofboards+arr[i]>threshold:
            painter+=1
            sumofboards=arr[i]
        else:
            sumofboards+=arr[i]
    return painter
def findLargestMinDistance(boards:list, k:int):
    n=len(boards)
    low=max(boards)
    high=sum(boards)
    while low<=high:
        mid=(low+high)//2
        if count(boards,mid)>k:
            low=mid+1
        else:
            high=mid-1
    return low
boards=[2,1,5,6,2,3]
k=2
print(findLargestMinDistance(boards,k))