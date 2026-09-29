"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]"""

strs=input()
seen={}
for s in strs:
    s1="".join(sorted(s))
    if s1 in seen.keys():
        seen[s1].append(s)
    else:
        seen[s1]=[s]
print(list(seen.values()))

#time=O(n)
#Space=O(n)