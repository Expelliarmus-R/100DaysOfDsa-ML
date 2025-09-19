import math
def maxx(arr):
    n=len(arr)
    maxi=float('-inf')
    for i in range(n):
        maxi=max(maxi,arr[i])
    return maxi

def totalhours(arr,hours):
    n=len(arr)
    thours=0
    for i in range(n):
        thours+=math.ceil(arr[i]/hours)
    return thours

def mink(nums,h):
    n=len(nums)
    m=maxx(nums)
    low=1
    high=m
    while low<=high:
        mid=(low+high)//2
        total=totalhours(nums,mid)
        if total<=h:
            high=mid-1
        else:
            low=mid+1
    return low
nums=[7,15,6,3]
h=8
print(mink(nums,h))