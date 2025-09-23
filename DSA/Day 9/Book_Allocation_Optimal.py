def cnt(arr,m,pages):
    student=1
    studentpages=0
    n=len(arr)
    for i in range(n):
        if studentpages+arr[i]<=pages:
            studentpages+=arr[i]
        else:
            student+=1
            studentpages=arr[i]
    return student
def bookallocation(arr,m):
    n = len(arr)
    if m > n:
        return -1
    low=max(arr)
    high=sum(arr)

    while low<=high:
        mid=(low+high)//2
        if cnt(arr, m, mid)==m:
            return mid
        elif cnt(arr, m, mid)>m:
            low=mid+1
        else:
            high=mid-1
    return low
arr=[25, 46, 28, 49, 24]
m=4
print(bookallocation(arr,m))
