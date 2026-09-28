"""Given a string s which may contain lowercase and uppercase characters. The task is to remove all duplicate characters from the string and find the resultant string. The order of remaining characters in the output should be same as in the original string.

Examples:

Input: s = "geEksforGEeks"
Output: "geEksforG"
Explanation: After removing duplicate characters such as E, e, k, s, we have string as "geEksforG"."""


s=input()
seen=[]
for i in range(len(s)):
	if s[i] not in seen:
	    seen.append(s[i])
print("".join(seen))

#Time=O(n)
#Space=O(k)