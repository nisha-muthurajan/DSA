"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

prices=list(map(int,input().split()))
min=prices[0]
profits=[]
for i in range(len(prices)):
    if prices[i]<min:
        min=prices[i]
    if prices[i]>min:
        profit=prices[i]-min
        profits.append(profit)
if profits:
    print(max(profits))
else:
     print(0)