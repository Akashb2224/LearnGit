file = open(r'C:\Users\akash\OneDrive\Desktop\New Text Document.txt',"w")

file.write("This is my first line\n")
file.write("This is my second line\n")
file.write("This is my third line")

file.close()

file_path=(r'C:\Users\akash\OneDrive\Desktop\New Text Document.txt')
file_path = open(file_path, mode='r')  # Open file in read mode
content = file_path.read()  # Read the entire content of the file

file_path.close()

print(content)