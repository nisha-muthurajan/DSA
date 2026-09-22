"""Given an array arr, find the floor of average of the prefix array at every index. 

Examples:

Input: arr[] = [10, 20, 30, 40, 50]
Output: [10, 15, 20, 25, 30] 
Explanation: 10 / 1 = 10, (10 + 20) / 2 = 15, (10 + 20 + 30) / 3 = 20 and so on.
Input: arr[] = [12, 1]
Output: [12, 6] """

arr=list(map(int,input().split()))
res=[]
total=0
for i in range(len(arr)):
    total+=arr[i]
    avg=total// (i+1)
    res.append(avg)
print(res)

#time complexity=o(n)
#space complexity=o(n)