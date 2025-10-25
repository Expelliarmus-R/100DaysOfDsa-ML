def summ(n):
    if n==0:
        return 1
    return n * summ(n-1)
n=int(3)
print(summ(n))