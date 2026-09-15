
"""```'''
Question:
Given n employee IDs determine wether all IDs are unique;
print YES if every ID occurs once else NO.

Constrains:
- Input will be numeric
'''

def uniqueEmpID():
    listOfEmpIDs = list(map(int, input("Enter the Employee IDs : ").split()))```
    print ("YES" if len(listOfEmpIDs) == len(set(listOfSetOfEmpIDs)) else "NO")"""
id=list(map(int,input().split()))
unique=True
uni_values=[]
for i in id:
    if i not in uni_values:
        uni_values.append(i)
    elif i in uni_values:
        unique=False
print("Yes") if unique==True else print("No")