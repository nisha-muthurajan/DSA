"""You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums."""
nums=list(map(int,input().split()))
freq={}
total=0
for i in nums:
    freq[i]=freq.get(i,0)+1
for i in freq:
    if freq[i]==1:
        total+=i
print(total)