"""
print names of students with more than
six quiz scores
"""
with open('studentdata.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        name = parts[0]
        scores = list(map(int, parts[1:]))

        if len(scores)>6:
            print(name)