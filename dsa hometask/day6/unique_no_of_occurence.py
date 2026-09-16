"""Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise."""
arr=list(map(int,input().split()))
freq={}
freq_occurence={}
unique=True
for i in arr:
    freq[i]=freq.get(i,0)+1
for i in freq.values():
    freq_occurence[i]=freq_occurence.get(i,0)+1
for i in freq_occurence:
    if freq_occurence[i]!=1:
        unique=False
print(unique)