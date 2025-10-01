def reverse(li,l,r):
    while l<r:
        li[l],li[r]=li[r],li[l]
        l+=1
        r-=1
def reversewords(s):
    li=list(s)
    n=len(li)
    reverse(li, 0, n - 1)
    start=0
    for i in range(n+1) :
        if i==n or li[i]==" ":
            reverse(li,start,i-1)
            start=i+1
    return "".join(li)
s="hello world"
print(reversewords(s))
