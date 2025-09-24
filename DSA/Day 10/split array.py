def check(arr,sum):
    n=len(arr)
    cnt=1
    sumofone=0
    for i in range(n):
        if sumofone+arr[i]>sum:
            cnt+=1
            sumofone=arr[i]
        else:
            sumofone+=arr[i]
    return cnt
def splitarray(arr,k):
    low=max(arr)
    high=sum(arr)
    n=len(arr)
    while low<=high:
        mid=(low+high)//2
        if check(arr,mid)>k:
            low=mid+1
        else:
            high=mid-1
    return low
arr=[10,20,30,40]
k=2
s=splitarray(arr,k)
print(s)
