a = input()
b = input()

fre_a = [0] * 26
fre_b = [0] * 26

for i in a:
    index = ord(i) - ord('a')
    fre_a[index] += 1

for i in b:
    index = ord(i) - ord('a')
    fre_b[index] += 1

is_match = True

for i in range(26):
    if fre_a[i] > fre_b[i]:
        is_match = False
        break

print(is_match)