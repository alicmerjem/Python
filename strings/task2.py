"""
count occurences of a spefific element
in the string
"""

def count_occurences(s, element):
    count = 0
    for char in s:
        if char == element:
            count += 1
    return count

text = 'programming'
char = 'a'
print(count_occurences(text, char))