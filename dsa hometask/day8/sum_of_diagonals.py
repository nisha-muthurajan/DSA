"""Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal."""

n=int(input())
mat=[]
for i in range(n):
    row=list(map(int,input().split()))
    mat.append(row)
total=0
n=len(mat)
for i in range(len(mat)):
    total+=mat[i][i]
    i+=1
for i in range(len(mat)):
    total+=mat[i][n-i-1]
    i+=1
if n%2!=0:
    center_index=n//2
    total-=mat[center_index][center_index]
    print(total)
else:
    print(total)

        
             
                

        