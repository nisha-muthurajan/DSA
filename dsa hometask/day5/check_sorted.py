arr=list(map(int,input().split()))
for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            print("False")
            break
else:
    print("True")