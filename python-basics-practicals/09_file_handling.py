with open("example.txt", "w") as f:
    f.write("Hello from Python file handling!")

with open("example.txt", "r") as f:
    print(f.read())
