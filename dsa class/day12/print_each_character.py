"""GET THE INPUT STRING FROM THE USER AND PRINT  THE INDEX WITH ITS CHARACTER"""

s=input()
for i in range(len(s)):
    print(f"{i} - {s[i]}")

#Time=O(n)
#Space=O(1)