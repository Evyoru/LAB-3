n = int(input())

for number in range(1, n + 1):
    original = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    if reversed_number == original:
        print(original)