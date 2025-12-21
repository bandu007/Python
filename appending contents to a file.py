# a is for appending
# If the file does not exist a mode creates the file
fh = open("file4.txt","at")

fh.write("\nThis file I have created using 'a' mode \n")
fh.write("a mode is used to add new content to the file\n")
fh.write("good bye")
fh.close()