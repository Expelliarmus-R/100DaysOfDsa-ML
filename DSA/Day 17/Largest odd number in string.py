def largestodd(s):
    n=len(s)
    for i in range(n-1,0,-1):
        if int(s[i])%2==1:
             return s[:i+1]
    return 0
s="5345"
print(largestodd(s))