"""Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers."""


s=input()
seen = set()
left = 0
max_length = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])
    max_length = max(max_length, right - left + 1)

print(max_length)

#time comlexity=0(n*m)
#space complexity=0(n)