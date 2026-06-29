try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("Error: The file was not found.")

finally:
    print("File not found error handling program completed.")
