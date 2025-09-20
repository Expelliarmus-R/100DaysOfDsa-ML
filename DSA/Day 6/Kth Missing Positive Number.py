def missing(arr,k):
    for i in range(len(arr)):
        if arr[i]<=k:
            k+=1
    return k
arr=[4,7,9,10]
k=1
s=missing(arr,k)
print(s)