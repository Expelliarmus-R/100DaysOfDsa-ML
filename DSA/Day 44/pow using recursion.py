def pow(x,n):
    if n==0:
        return 1
    return x*pow(x,n-1)
print(pow(4,3))