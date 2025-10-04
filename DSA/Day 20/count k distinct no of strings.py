def substringwithdistinctk(s,k):
    n=len(s)
    count=0
    for i in range(n):
        freq={}
        distinct=0
        for j in range(i,n):
            if s[j] not in freq or freq[s[j]]==0 :
                distinct+=1
                freq[s[j]]=1
            else:
                freq[s[j]]+=1
            if distinct==k:
                count+=1
            elif distinct>k:
                break
    return count
s="abababa"
k=2
print(substringwithdistinctk(s,k))
