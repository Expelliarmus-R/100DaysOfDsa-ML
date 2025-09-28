def medi(arr):
    n=len(arr)
    m=len(arr[0])
    ls=[]
    for i in range(n):
        for j in range(m):
            ls.append(arr[i][j])
    sorted(ls)
    return ls[m*n//2]
arr=[
   [1,2,3],
   [5,4,6],
   [7,8,9]
]
print(medi(arr))
