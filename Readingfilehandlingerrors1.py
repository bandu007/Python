file = "sample.txt"

try:
    with open(file) as fh:
        line1 = fh.readline()
        line2 = fh.readline()

    print(f"Line1:{line1}")
    print(f"line2:{line2}")

except FileNotFoundError :
    print(f"Error:The file '{file}' was not found")