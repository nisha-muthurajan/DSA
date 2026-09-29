"""Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg" """

s=input()
k=int(input())
s=list(s)
i=0
while i<len(s):
    left=i
    right=min(i+k-1,len(s)-1)

    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    i += k * 2
        

        
print("".join(s))

#Time=O(n^2)
#Space=O(1)
        