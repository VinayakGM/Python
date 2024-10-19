# f=open("file.txt")
# content=f.read()
# print(content)
# f.close()

with open("file.txt") as f:
    contents=f.read()
    print(contents)
# automatically closes the file after the loop

with open("file1.txt",mode="w") as f:
    f.write("hello world")

with open("file1.txt") as f:
    contents=f.read()
    print(contents)

with open("file.txt",mode="a") as f:
    f.write("hi Angela")

with open("file.txt") as f:
    contents=f.read()
    print(contents)



