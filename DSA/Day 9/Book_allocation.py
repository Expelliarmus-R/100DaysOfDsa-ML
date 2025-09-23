def cnt(arr,m,pages):
    studentpages=0
    student=1
    n=len(arr)
    for i in range(n):
        if studentpages+arr[i]<=pages:
            studentpages+=arr[i]
        else:
            student+=1
            studentpages=arr[i]
    return student
def bookallocation(arr,m):
    n=len(arr)

    if m > n:
        return -1
    low=max(arr)
    high=sum(arr)
    for i in range(low,high+1):
        if cnt(arr,m,i)==m:
            return i
    return low
arr=[25, 46, 28, 49, 24]
m=4
print(bookallocation(arr,m))