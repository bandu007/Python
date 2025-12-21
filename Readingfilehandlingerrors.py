
import os

file = "sample.txt"

if os.path.exists(file):


    with open(file, "rt") as fh:
        print("Reading file content")
        line1 = fh.readline()
        line2 = fh.readline()


    print(f"Line1:{line1}")
    print(f"line2:{line2}")
else:
    print(f"Error:The file '{file}' was not found")
    with open(file,"xt") as fh:
        fh.write("This is a sample text file. \n")
        fh.write("It contains multiple lines.")