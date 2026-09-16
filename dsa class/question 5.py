
"""Find The first non repeating element in the array"""
arr=list(input().split())
freq={}
for i in arr:
    freq[i]=freq.get(i,0)+1
for i in freq:
    if freq[i]==1:
        print(i)
        break
else:
    print("All elements are repeating")

         
 