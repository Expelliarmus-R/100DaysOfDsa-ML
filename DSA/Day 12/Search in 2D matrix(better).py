def search(matrix,k):
    n=len(matrix)
    m=len(matrix[0])
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        row=mid//m
        col=mid%m
        if matrix[row][col]==k:
            return True
        elif matrix[row][col]<k:
            low=mid+1
        else:
            high=mid-1
    return False
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = search(matrix, 99)
print(result)