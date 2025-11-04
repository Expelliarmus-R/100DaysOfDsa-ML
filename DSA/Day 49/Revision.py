# def largest_(arr):
#     maxi=-1
#     for i in arr:
#         if i > maxi :
#             maxi=i
#     return maxi
# arr=[1,2,3,4,5]
# print(largest_(arr))

# def slargest(arr):
#     largest,slar=float('-inf'),float('-inf')
#     for i in arr:
#         if i > largest:
#             slar=largest
#             largest=i
#         if i > slar and i!=largest:
#             slar=i
#     return slar
# arr=[11,34,2,4,5]
# print(slargest(arr))
# def sortedarr(arr):
#     for i in range(1,len(arr)):
#         if arr[i-1]>arr[i]:
#             return False
#     return True
# arr=[1,2,3,4,3]
# print(sortedarr(arr))
# def remove(arr):
#     st=set()
#     for i in range(len(arr)):
#         st.add(arr[i])
#     k=len(st)
#     j=0
#     for x in st:
#         arr[j]=x
#         j+=1
#     for i in range(k):
#         print(arr[i])
#
# arr=[11,2,3,4,4,5,6,6]
# remove(arr)
# def remove(arr):
#     i=0
#     for j in range(1,len(arr)):
#         if arr[i]!=arr[j]:
#             i += 1
#             arr[i]=arr[j]
#
#     return i+1
# arr=[1,1,1,1,2,2,2,4]
# print(remove(arr))

# def leftrotate(arr):
#     temp=arr[0]
#     n=len(arr)
#     for i in range(n-1):
#         arr[i]=arr[i+1]
#     arr[n-1]=temp
#     for i in range(n):
#         print(arr[i])
# arr=[1,2,3,4,5]
# print(leftrotate(arr))


# def leftrotate(arr,d):
#     n=len(arr)
#     d=d%n
#     temp=arr[:d]
#     for i in range(d,n):
#         arr[i-d]=arr[i]
#     for i in range(n-d,n):
#         arr[i]=temp[i-(n-d)]
#     for i in range(n):
#         print(arr[i])
# arr=[1,2,3,4,5]
# print(leftrotate(arr,3))
# def reversef(arr,start,end):
#     while start<=end:
#         arr[start],arr[end]=arr[end],arr[start]
#         start+=1
#         end-=1
# def leftrotate(arr,d):
#     n=len(arr)
#     d=d%n
#     reversef(arr,0,d-1)
#     reversef(arr,d,n-1)
#     reversef(arr,0,n-1)
#     return arr
# arr=[1,4,6,7,7]
# print(leftrotate(arr,3))

# def movezeroes(arr):
#     n=len(arr)
#     ans=[]
#     for i in range(n):
#         if arr[i]!=0:
#             ans.append(arr[i])
#     z=len(ans)
#     x=0
#     for i in range(z):
#         arr[i]=ans[i]
#     for i in range(z,n):
#         arr[i]=0
#
#     return arr
# arr=[1,2,4,0,5,6,0,7,0,77]
# print(movezeroes(arr))

# def movezeros(arr):
#     j=-1
#     n=len(arr)
#     for i in range(len(arr)):
#         if arr[i]==0:
#             j=i
#             break
#     if j== -1:
#         return arr
#     for i in range(j+1,n):
#         if arr[i]!=0:
#             arr[i],arr[j]=arr[j],arr[i]
#             j+=1
#     return arr
# arr=[1,0,2,0,0,0,3,4,5]
# print(movezeros(arr))

# def union(arr1,arr2):
#     s=set()
#     union=[]
#     for i in arr1:
#         s.add(i)
#     for i in arr2:
#         s.add(i)
#     for i in s:
#         union.append(i)
#     return union
# arr1=[2,3,5]
# arr2=[5,4,3]
# print(union(arr1,arr2))
#
# def findunion(arr1,arr2):
#     l=[]
#     i,j=0,0
#     while i<len(arr1) and j<len(arr2):
#         if arr1[i]<=arr2[j]:
#             if len(l)==0 or l[-1]!=arr1[i]:
#                 l.append(arr1[i])
#             i+=1
#         else:
#             if len(l)==0 or l[-1]!=arr2[j]:
#                 l.append(arr2[j])
#             j+=1
#     while i<len(arr1):
#         if l[-1]!=arr1[i]:
#             l.append(arr1[i])
#         i+=1
#     while j<len(arr2):
#         if l[-1]!=arr2[j]:
#             l.append(arr2[j])
#         j+=1
#     return l
# arr1=[1,2,3]
# arr2=[3,4,6]
# print(findunion(arr1,arr2))
import math
# def findmissing(arr):
#     n=max(arr)
#     s1=(n*(n+1))//2
#     s2=sum(arr)
#     missing=s1-s2
#     return missing
# arr=[1,2,4,5]
# print(findmissing(arr))

# def maxcons(arr):
#     n=len(arr)
#     maxi=0
#     cnt = 0
#     for i in range(n):
#
#         if arr[i]==1:
#             cnt+=1
#             maxi=max(maxi,cnt)
#         else:
#             cnt=0
#     return maxi
# arr=[1,1,1,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1]
# print(maxcons(arr))

# def find(arr):
#     n=len(arr)
#     for i in range(n):
#         cnt=0
#         for j in range(n):
#             if arr[i]==arr[j]:
#                 cnt+=1
#         if cnt==2:
#             return arr[i]
#     return -1
# arr=[1,2,2,3,4,4,3,2]
# print(find(arr))

# def find(arr):
#     mp={}
#     for i in range(len(arr)):
#         if arr[i] in mp:
#             mp[arr[i]]+=1
#         else:
#             mp[arr[i]]=1
#     for key,value in mp.items():
#         if value==1:
#             print( key)
#     return
# arr=[1,2,2,3,4,5]
# print(find(arr))

# def longestsubarray(arr,k):
#     n=len(arr)
#     length=0
#     for i in range(n):
#         sum=0
#         for j in range(i,n):
#             sum+=arr[j]
#             if sum==k:
#                 length=max(length,j-i+1)
#     return length
# arr=[2,3,5,1,9]
# print(longestsubarray(arr,10))

# def twosum(arr,target):
#     n=len(arr)
#     for i in range(n):
#         for j in range(i,n):
#             if arr[i]+arr[j]==target:
#                 return i,j
#     return -1
# arr=[1,7,2,3,4]
# print(twosum(arr,5))
#
# def twosum(arr,target):
#     n=len(arr)
#     mp={}
#     ans=[-1,-1]
#     for i in range(n):
#         more=target-arr[i]
#         if more in mp :
#             ans[0]=mp[more]
#             ans[1]=i
#             return ans
#         mp[arr[i]]=i
#     return ans
# arr=[1,2,5,2,3]
# print(twosum(arr,5))

# def sort0s(arr):
#     n=len(arr)
#     mid=0
#     low=0
#     high=n-1
#     while mid<=high:
#         if arr[mid]==0:
#             arr[low],arr[mid]=arr[mid],arr[low]
#             mid+=1
#             low+=1
#         elif arr[mid]==1:
#             mid+=1
#         else:
#             arr[mid],arr[high]=arr[high],arr[mid]
#             high-=1
#     return arr
# arr=[1,0,2,1,1,1,0,2]
# print(sort0s(arr))

