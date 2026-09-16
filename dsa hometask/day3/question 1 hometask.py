"""Q1:
Problem Statement
Create a 1-D array to store a set of exam scores. Write a program to perform the following operations:
1.Display the scores in rows of four scores per row. 
2.Calculate and display the average score. 
3.Find and display the lowest score. 
4.Find and display the highest score. 
5.Calculate the deviation of each score from the average and display the score along with its deviation. 
6.Calculate and display the standard deviation. 
7.Count and display how many scores are within one standard deviation of the average. """
# cook your dish here
import math


n = int(input())
scores = list(map(int, input().split()))

print("Scores:")
for i in range(n):
    print(scores[i], end=" ")
    if (i + 1) % 4 == 0:
        print()



total = sum(scores)
average = total / n

print()
print(f"Average: {average:.2f}")



lowest = min(scores)
print(f"Lowest Score: {lowest}")



highest = max(scores)
print(f"Highest Score: {highest}")



print()
print("Score  Deviation")

sum_squared_deviation = 0

for score in scores:
    deviation = score - average
    print(f"{score:<6}{deviation:>7.2f}")
    
    sum_squared_deviation += deviation ** 2



sd = math.sqrt(sum_squared_deviation / n)

print()
print(f"Standard Deviation: {sd:.2f}")



count = 0

for score in scores:
    if average - sd <= score <= average + sd:
        count += 1

print()
print(f"Scores within one standard deviation: {count}")
