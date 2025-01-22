"""
calculate and print min and max score
for each student
"""
with open('studentdata.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        name = parts[0]
        scores = list(map(int, parts[1:]))

        min_score = min(scores)
        max_score = max(scores)
