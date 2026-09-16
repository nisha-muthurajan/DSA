"""Find the minimum and maximum in the array"""
arr=list(map(int,input().split()))
minimum=arr[0]
maximum=arr[0]
for i in arr:
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i
print(minimum, maximum)