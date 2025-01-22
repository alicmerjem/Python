"""
calculate and print average grade for
each student
"""
with open('studentdata.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        name = parts[0]
        scores = list(map(int, parts[1:]))

        avg_score = sum(scores) / len(scores)
        