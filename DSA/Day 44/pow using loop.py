def pow(x,n):
    res=1
    for i in range(1,n+1):
        res=res*x
    return res
print(pow(4,3))