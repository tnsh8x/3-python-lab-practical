"""Experiment 10: file manipulation - open, close, read, write, append
and copy the contents of one file into another."""

# 1. Open in write mode and write
f = open("source.txt", "w")
f.write("Hello, this is the first line.\n")
f.write("Python file handling is easy.\n")
f.close()
print("1. source.txt created and written")

# 2. Append
f = open("source.txt", "a")
f.write("This line was appended.\n")
f.close()
print("2. Line appended to source.txt")

# 3. Read (whole file, one line, all lines)
f = open("source.txt", "r")
print("3. read() whole file:")
print(f.read())
f.seek(0)
print("   readline():", f.readline().strip())
f.seek(0)
print("   readlines():", f.readlines())
f.close()

# 4. Copy source.txt to destination.txt
with open("source.txt", "r") as src, open("destination.txt", "w") as dst:
    dst.write(src.read())
print("4. Content copied to destination.txt")

# 5. Verify the copy and show closed status
with open("destination.txt", "r") as f:
    print("5. destination.txt contains:")
    print(f.read())
print("   File closed automatically by 'with':", f.closed)
