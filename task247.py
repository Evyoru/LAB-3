n = int(input())

total = 0
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i
    total = total + factorial

print(total)