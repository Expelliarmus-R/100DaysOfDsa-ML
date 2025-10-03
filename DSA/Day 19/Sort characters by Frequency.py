def sortbyfreq(s):
    mp={}
    for i in range(len(s)):
        mp[s[i]]=mp.get(s[i],0)+1

    groups={}
    for ch,count in mp.items():
        groups.setdefault(count,[]).append(ch)
    result=[]
    for count in sorted(groups.keys(),reverse=True):
        for ch in sorted(groups[count]):
            result.append(ch*count)
    return "".join(result)
s="heyy"
print(sortbyfreq(s))