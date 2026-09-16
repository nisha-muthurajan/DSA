"""Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1."""

s=input()
freq={}
for i in s:
    freq[i]=freq.get(i,0)+1
for i in freq:
    if freq[i]==1:
         print(s.index(i))
         break
else:
     print(-1)
        