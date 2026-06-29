try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)

except ValueError:
    print("Error: Please enter a valid number.")

finally:
    print("Value error handling program completed.")
