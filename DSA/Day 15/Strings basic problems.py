# count characters
# def strin(s):
#     cnt=0
#     for i in s :
#         cnt+=1
#     return cnt
# s="malayalam"
# print(strin(s))

# count spaces
# def strin(s):
#     cnt=0
#     for i in s :
#         if i==" ":
#             cnt+=1
#     return cnt
# s=" hello im rakesh kumar "
# print(strin(s))

# Reverse a string
# def reverse(s):
#     s=list(s)
#     n=len(s)
#     left=0
#     right=n-1
#     while left<right:
#         s[left],s[right]=s[right],s[left]
#         left+=1
#         right-=1
#     return "".join(s)
#
# s="hello"
# print(reverse(s))

#check palindrome using slicing
# def palindrome(s):
#     if s==s[::-1]:
#         return True
#     return False
# s="hello"
# print(palindrome(s))

# #using while loop
# def palindrome(S):
#     low=0
#     high=len(s)-1
#     while low<high:
#         if s[low]!=s[high]:
#             return False
#     return True
# print(palindrome("super"))

# toggle upper and lower
# def toggle(s):
#     res=""
#     k={"k","i","h"}
#     for i in s :
#         if i.lower() in k:
#             res+=i.upper()
#         else:
#             res+=i
#     return res
# s="hey,iam,working"
# print(toggle(s))

# Find frequency of each character
# def findchar(s):
#     mp={}
#     for i in s:
#         if i in mp:
#             mp[i]+=1
#         else:
#             mp[i]=1
#     return mp
# s= "salaar"
# print(findchar(s))

# Remove all duplicate characters.
# def remove(s):
#     st=set()
#     for i in s:
#         st.add(i)
#     return st
# s="heybroooo"
# print(remove(s))

#2 way
# def remove(s):
#     res=s[0]
#     for i in s[1:]:
#         if i!=res[-1]:
#             res+=i
#     return res
# s="aabbcc"
# print(remove(s))

# Find the first non-repeating character.
# def repeating(s):
#     mp={}
#     for i in s:
#         mp[i]=mp.get(i,0)+1
#     for ch in s:
#         if mp[ch]==1:
#             return ch
#     return -1
# s="aabbacccd"
# print(repeating(s))

# Replace all spaces with a given character (e.g., -)

# def removesp(s):
#     r=""
#     r=s.replace(" ","")
#     return r
# s="r a k e s h"
# print(removesp(s))

# def removes(s):
#     c=""
#     res=""
#     for i in s:
#         if i==" ":
#             res+=c
#         else:res+=i
#     return res
# s="r a k e s h"
# print(removes(s))

# Remove vowels from a string.
# def removevowels(s):
#     res=""
#     ch=""
#     for i in s :
#         if i =="a" or i=="e" or i=="i" or i=="o" or i=="u":
#             res+=ch
#         else:
#             res+=i
#     return res
# s="rakeshkumar"
# print(removevowels(s))

# Remove all occurrences of a given character
# def removeall(s):
#     res=""
#     ch=""
#     for i in s :
#         if i =="k":
#             res+=ch
#         else:
#             res+=i
#     return res
# s="kingkohli"
# print(removeall(s))

# Check if two strings are anagrams
# def anagram(s1,s2):
#     s1=list(s1)
#     s2=list(s2)
#     s1.sort()
#     s2.sort()
#     if s1==s2:
#         return True
#     else:
#         return False
# s1="mug"
# s2="gum"
# print(anagram(s1,s2))
#2
# from collections import Counter
# def anagram(s1,s2):
#     return Counter(s1)==Counter(s2)
# s1="mug"
# s2="gum"
# print(anagram(s1,s2))

# Count the number of words in a string.
# def count(s):
#     cnt=0
#     for i in s:
#         if i.isdigit():
#             cnt+=1
#     return cnt
# s="rakesh12345"
# print(count(s))