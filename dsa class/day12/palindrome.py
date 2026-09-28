"""Check whether the given input is palindrome or not"""

s=input()
left=0
right=len(s)-1
palindrome=True
while left<right:
    if s[left]!=s[right]:
        palindrome=False
        break
    left+=1
    right-=1
print(palindrome)


#Time=O(n)
#Space=O(1)

