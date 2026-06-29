def is_perfect_number(n):
    if n <= 1:
        return False

    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i

    return divisor_sum == n


while True:
    try:
        num = int(input("Enter a number (-1 to exit): "))

        if num == -1:
            print("Goodbye!")
            break

        if is_perfect_number(num):
            print(f"{num} is a perfect number.")
        else:
            print(f"{num} is not a perfect number.")

    except ValueError:
        print("Please enter a valid integer.")
