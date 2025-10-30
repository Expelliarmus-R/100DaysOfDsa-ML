def comb(arr,target):
    ans=[]
    def backtrack(index,target,ds):
        if index==len(arr):
            if target==0:
                ans.append(ds[:])
            return
        if arr[index]<=target:
            ds.append(arr[index])
            backtrack(index,target-arr[index],ds)
            ds.pop()
        backtrack(index+1,target,ds)
    backtrack(0,7,[])
    return ans
print(comb([2,3,6,7],7))
