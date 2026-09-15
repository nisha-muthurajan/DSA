"""print the first and second largest number in the given array"""

arr=list(map(int,input().split(" ")))
print(arr)
maximum=arr[0]
for i in range(1,len(arr)):
    if arr[i]>maximum:
        maximum=arr[i]
        max_index=i
print("first largest:",maximum,"index:",max_index+1 )

sec_maximum=arr[0]
for j in range(1,len(arr)):
    if arr[j]>sec_maximum and arr[j]<maximum:
        sec_maximum=arr[j]
        sec_index=j
print("second largest:",sec_maximum,"index:",sec_index+1)