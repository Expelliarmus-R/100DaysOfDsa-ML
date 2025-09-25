def ninjaAndLadoos(row1, row2, m, n, k):
    cnt = 0
    index = k - 1
    indexel = -1
    i, j = 0, 0
    while i < m and j < n:
        if row1[i] < row2[j]:
            if cnt == index:
                indexel = row1[i]
            cnt += 1
            i += 1
        else:
            if cnt == index:
                indexel = row2[j]
            cnt += 1
            j += 1
    while i < m:
        if cnt == index:
            indexel = row1[i]
        cnt += 1
        i += 1

    while j < n:
        if cnt == index:
            indexel = row2[j]
        cnt += 1
        j += 1
    return indexel


row1=[1,2,3]
row2=[4,5,6]
m=len(row1)
n=len(row2)
k=4
print(ninjaAndLadoos(row1,row2,m,n,k))