"""Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order.

Examples:

Input: s1 = "geeks" s2 = "kseeg"
Output: true 
Explanation: Both the string have same characters with same frequency. So, they are anagrams."""
s1=input()
s2=input()
freq1={}
freq2={}
for i in s1:
    freq1[i]=freq1.get(i,0)+1
for j in s2:
    freq2[j]=freq2.get(j,0)+1
print(freq1==freq2)

#Time=O(n)
#Space=O(n)