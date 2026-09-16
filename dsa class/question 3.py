
"""In teh guven array and the tagret element find the number of occurance of the target element"""
arr=list(input().split())
t=input()
count=0
for i in arr:
    if t==i:
        count+=1
if count:
    print(count)
else:
    print("The Target",t,"is not found")