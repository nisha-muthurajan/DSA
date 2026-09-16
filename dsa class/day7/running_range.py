"""find the running range of the given array"""

n=int(input())
arr=list(map(int,input().split()))
maximum=arr[0]
minimum=arr[0]
for i in arr:
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i
        
    ran=maximum-minimum
    print(ran,end=" ")