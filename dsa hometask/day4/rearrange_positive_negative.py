# Rearrange positive and negative numbers alternately

arr = list(map(int, input("Enter positive and negative numbers: ").split()))

positive = []
negative = []

for value in arr:
    if value >= 0:
        positive.append(value)
    else:
        negative.append(value)

positive_index = 0
negative_index = 0
array_index = 0

while positive_index < len(positive) and negative_index < len(negative):
    if array_index % 2 == 0:
        arr[array_index] = positive[positive_index]
        positive_index += 1
    else:
        arr[array_index] = negative[negative_index]
        negative_index += 1
    array_index += 1

while positive_index < len(positive):
    arr[array_index] = positive[positive_index]
    positive_index += 1
    array_index += 1

while negative_index < len(negative):
    arr[array_index] = negative[negative_index]
    negative_index += 1
    array_index += 1

print("Rearranged array:", arr)
