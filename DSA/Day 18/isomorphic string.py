def isomorophic(s,t):
    m1=[-1]*256
    m2=[-1]*256
    n=len(s)
    for i in range(n):
        if m1[ord(s[i])]!=m2[ord(t[i])]:
            return False
    m1[ord(s[i])]=i+1
    m2[ord(t[i])]=i+1
    return True
s="paper"
t="title"
print(isomorophic(s,t))
