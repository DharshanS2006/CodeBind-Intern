try:
    number = 10
    text = "5"

    result = number + int(text)
    print("Result:", result)

except TypeError:
    print("Error: Cannot add a number and a string together.")

finally:
    print("Type error handling program completed.")
