def rotationstring(s,goal):
    double=s+s
    if len(s)!=len(goal):
        return False
    if goal in double:
        return True
    return False
s="rotation"
goal="tionrota"
print(rotationstring(s,goal))
