def string(s):
    res=""
    for i in s:
        if i!='a' and i!="e" and i!="i" and i!="o" and i!="u":
            res+=i
    return res
s="aeiourksh"
print(string(s))
