import math
def divisor(arr,c):
    sumi=0
    for i in range(len(arr)):
        sumi+=math.ceil(arr[i]/c)
    return sumi
def smallest(arr,threshold):
    low=1
    high=max(arr)
    while low <= high:
        mid=(low+high)//2
        if divisor(arr,mid)<=threshold:
            high=mid-1
        else:
            low=mid+1
    return low
arr=[8,4,2,3]
threshold=10
s=smallest(arr,threshold)
print(s)
