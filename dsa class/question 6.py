"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""
nums=list(map(int,input().split()))
freq={}

for i in nums:
    freq[i]=freq.get(i,0)+1
for i in freq:
    if freq[i]>1:
        print(True)
        break
else:
    print(False)