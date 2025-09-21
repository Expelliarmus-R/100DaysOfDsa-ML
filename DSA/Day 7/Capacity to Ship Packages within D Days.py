import math
def capacity(weights,c):
    load=0
    days=1
    n=len(weights)
    for i in range(n):
        if load+weights[i]>c:
            days+=1
            load=weights[i]
        else:
            load+=weights[i]
    return days
def ship(weights,d):
    n=len(weights)
    low=min(weights)
    high=sum(weights)
    while low<=high:
        mid=(low+high)//2
        if capacity(weights,mid)<=d:
            high=mid-1
        else:
            low=mid+1
    return low

weights=[5,4,5,2,3,4,5,6]
d=5
print(ship(weights, d))