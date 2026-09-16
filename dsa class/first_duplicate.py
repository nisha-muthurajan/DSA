"""find the first duplicate in the given array"""

arr=list(map(int,input().split()))
seen=set()
for i in arr:
    if i in seen:
        print(i)
        break
    seen.add(i)
