
"""Find The frequency of every element in the array"""
arr=list(input().split())
freq={}
for i in arr:
    """if i in freq:
        freq[i]+=1
    else:
        freq[i]=1"""
    freq[i]=freq.get(i,0)+1
print(freq)
         
