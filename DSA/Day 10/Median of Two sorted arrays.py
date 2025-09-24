def median(a,b):
    n1=len(a)
    n2=len(b)
    n=n1+n2
    index2=n//2
    index1=index2-1
    ind1el,ind2el=-1,-1
    found1,found2=False,False
    i,j=0,0
    temp=[]
    cnt=0
    while i < n1 and j < n2 :
        if a[i]<b[j]:
            if cnt==index1:
                ind1el=a[i]
                found1=True
            if cnt==index2:
                ind2el=a[i]
                found2=True
            cnt+=1
            i+=1
        else:
            if cnt==index1:
                ind1el=b[j]
                found1=True
            if cnt==index2:
                ind2el=b[j]
                found2=True
            cnt+=1
            j+=1
        if found1 and found2:
            break
    if not (found1 and found2):
        while i < n1 :
            if cnt==index1:
                ind1el=a[i]
                found1=True
            if cnt==index2:
                ind2el=a[i]
                found2=True
            cnt+=1
            i+=1
        while j < n2:
            if cnt==index1:
                ind1el=b[j]
                found1=True
            if cnt==index2:
                ind2el=b[j]
                found2=True
            cnt+=1
            j+=1

    if n%2 == 1:
        return float(ind2el)
    median=float(ind2el+ind1el)/2.0
    return median
a = [1, 5, 9, 10]
b = [2, 3, 6, 7, 11]
s=median(a,b)
print(s)






