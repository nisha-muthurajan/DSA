"""Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice."""
nums=list(map(int,input().split()))
freq={}
ans=[]
for i in nums:
    freq[i]=freq.get(i,0)+1
for i in freq:
    if freq[i]==2:
        ans.append(i)
print(ans)