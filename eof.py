try:
    name = input("Enter your name: ")
    print("Hello, " + name)
except EOFError:
    print("Error: End of file reached")