content = "This is going to be in my text file"

with open("myfile.txt", "+w") as f:
    for i in range(70):
        f.write(content + "\n")
    
print("Success")