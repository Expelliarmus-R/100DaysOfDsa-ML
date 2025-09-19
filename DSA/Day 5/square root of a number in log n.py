def squareroot(n):
    low=1
    high=n
    while low<=high:
        mid=(low+high)//2
        pow=mid*mid
        if pow <= n:
            low=mid+1
        else:
             high=mid-1
    return high
n=36
s=squareroot(n)
print(s)
