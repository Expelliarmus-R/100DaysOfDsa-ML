def subs(s, ind, ds,arr):
    if ind == len(arr):
        if s==sum:
            print(ds)
        return

    ds.append(arr[ind])
    subs(s+arr[ind], ind + 1, ds,arr)
    ds.pop()
    subs(s,ind + 1, ds,arr)


arr = [3, 2, 1]
sum=3
print(subs(0, 0, [],arr))
