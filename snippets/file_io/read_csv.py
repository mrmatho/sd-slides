with open("data.csv","r") as file:
    header = file.readline()
    for line in file:
        parts = line.strip().split(",")
        print(parts[0], parts[1])
