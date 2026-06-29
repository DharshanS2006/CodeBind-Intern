num = input("Enter a number: ")

total = 0

for digit in num:
    total += int(digit)

print(f"Sum of digits: {total}")
