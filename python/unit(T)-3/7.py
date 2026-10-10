import shutil
import os

# Create a sample file
with open("source.txt", "w") as f:
    f.write("Hello, Python!")

# 1. Copy the file
shutil.copy("source.txt", "copy.txt")
print("File copied successfully.")

# 2. Move the file
shutil.move("copy.txt", "moved.txt")
print("File moved successfully.")

# 3. Delete the file
os.remove("moved.txt")
print("File deleted successfully.")
