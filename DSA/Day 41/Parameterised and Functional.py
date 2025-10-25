# def summ(i,s):
#     if i>3:
#         print(s)
#         return
#     summ(i+1,s+i)
# print(summ(0,0))

def summ(n):
    if n==0:
        return 0
    return n + summ(n-1)
n=int(3)
print(summ(n))
