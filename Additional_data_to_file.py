data1 = input("Enter text to write to the file: ")

file = "output.txt"

with open(file,"wt") as fh:
    fh.write(data1)
    print("Data successfully written to output.txt")

data2 = input("Enter additional text to append :")

with open(file,"at") as fh:
    fh.write('\n')
    fh.write(data2)

with open(file,"rt") as fh:
    output = fh.read()

print(f"Final content of {file}:")
print(output)