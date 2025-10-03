def maxdepth(s):
    cnt=0
    maxi=0
    for i in s:
        if i=="(":
            cnt+=1
            maxi=max(maxi,cnt)
        elif i==")":
            cnt-=1
    return maxi
s="((1)(2)((3)))"
print(maxdepth(s))
