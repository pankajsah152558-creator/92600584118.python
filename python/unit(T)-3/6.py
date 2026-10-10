import os
import sys

# Display current working directory
print("Current Directory:", os.getcwd())

# Create a new directory
if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")
    print("Directory created successfully.")

# Create and write to a file
with open("MyFolder/demo.txt", "w") as f:
    f.write("Hello, Python!")

print("File created successfully.")

# Read the file
with open("MyFolder/demo.txt", "r") as f:
    print("File Content:", f.read())

# List files and directories
print("Directory Contents:", os.listdir("MyFolder"))

# Display Python version
print("Python Version:", sys.version)

# Display command-line arguments
print("Command-line Arguments:", sys.argv)
