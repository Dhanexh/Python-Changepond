try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: An I/O error occurred while reading the file.")
except Exception as e:
    print(f"Unexpected error: {e}")
