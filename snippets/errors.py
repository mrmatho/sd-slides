
sports = ["Football", "Basketball", "Baseball", "Hockey", "Tennis"]

tic_tac_toe = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "O", "X"]
]

city = {
    "name": "New York",
    "population": 8419000,
    "country": "USA"
}

student = {
    "name": "Geoffrey", 
    "age": 42,
    "favourite_subjects": ["Software Development",
                           "Maths", 
                           "Economics"],
}

name = student["name"]
subs = student["favourite_subjects"]

for subject in subs:
    print(name + " likes " + subject + ".")

for row in tic_tac_toe:
    print("-----")
    print(row[0] + " | " + row[1] + " | " + row[2])
    