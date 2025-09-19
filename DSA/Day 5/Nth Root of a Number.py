def nthroot(n,m):
    low=1
    high=m
    while low<=high:
        mid=(low+high)//2
        pow=mid**n
        if pow==m:
            return mid
        if pow<m:
            low=mid+1
        else:
            high=mid-1
    return -1
n,m=3,27
print(nthroot(n,m))
