def missing(arr):
    n=len(arr)
    sn=(n*(n+1))//2
    s2n=(n*(n+1)*(2*n+1))//6
    s1,s2=0,0
    for i in range(n):
        s1+=arr[i]
        s2+=arr[i]*arr[i]
    val1=s1-sn
    val2=s2-s2n
    val2=val2//val1
    x=(val1+val2)//2
    y=x-val1
    return [x,y]
arr=[1,2,3,4,4,5,6]
s=missing(arr)
print(s)
