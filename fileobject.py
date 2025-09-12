# f = open('file.txt', 'r')

# print(f.name)
# print(f.mode)
# print(f.read())

# f.close()

# with open('file.txt', 'r') as f:
#     f_contents = f.read()
   
#     print(f_contents)

# with open('file.txt', 'w') as f:
#     f.write("test")
    
#     f.write("R")
#     print(f_contents)

#copy the contents
with open('file.txt', 'r') as rf:
    with open('file2.txt', 'w') as wf:
        for line in rf:
            wf.write(line)