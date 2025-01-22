"""
given the string, perform the following
operations: 
- print the substring from index 3 to 7
- print the last 4 chars of the string
- concat s with is fun and print the
result
"""

s = 'programming'
substring = s[3:8]
print(substring)

last_four = s[-4:]
print(last_four)

concat = s + ' is fun!'
print(concat)