try:
    fruits = ["apple", "banana", "orange"]
    index = int(input("Enter an index number: "))

    print("Fruit at index", index, "is:", fruits[index])

except IndexError:
    print("Error: The index number is out of range.")

except ValueError:
    print("Error: Please enter a valid number.")

finally:
    print("Index error handling program completed.")
