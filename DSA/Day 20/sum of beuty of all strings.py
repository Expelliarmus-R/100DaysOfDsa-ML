def sumofbeauty(s):
    n=len(s)
    total=0
    for i in range(n):
        freq={}
        for j in range(i,n):
            freq[s[j]]=freq.get(s[j],0)+1

        values=freq.values()
        mini=min(values)
        maxi=max(values)
        total+=(maxi-mini)
    return total
s="xyx"
print(sumofbeauty(s))