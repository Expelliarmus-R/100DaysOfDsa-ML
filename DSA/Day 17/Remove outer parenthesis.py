def paren(s):
    balance=0
    res=""
    for i in s :
        if i=="(":
            if balance>0:
                res+=i
            balance+=1
        else:
            balance-=1
            if balance>0:
                res+=i
    return res
s="(())(())(())"
print(paren(s))