def longestcommonprefix(s):
    n=len(s)
    s=sorted(s)
    ans=[]
    s1=s[0]
    s2=s[n-1]
    for i in range(min(len(s1),len(s2))):
        if s1[i]!=s2[i]:
            return "".join(ans)
        ans.append(s1[i])
    return "".join(ans)
s=["flower","flow","flight"]
print(longestcommonprefix(s))