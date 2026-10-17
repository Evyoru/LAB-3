index = 0
max_value = 0
max_index = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n > max_value:
        max_value = n
        max_index = index
    index = index + 1

print(max_index)