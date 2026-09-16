"""Find the average of the odd and even numbers in the given array"""

arr=list(map(int,input().split()))
odd_sum=0
odd_count=0
even_sum=0
even_count=0
for i in arr:
    if i%2==0:
        even_sum+=i
        even_count+=1
    else:
        odd_sum+=i
        odd_count+=1
print("Average of odd numbers:",odd_sum/odd_count)
print("Average of even numbers:",even_sum/even_count)