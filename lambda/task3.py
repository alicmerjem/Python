"""
lambda function for counting the 
occurence of a char in a string, but 
only if the string is more than 10
chars long
"""
char_count = lambda s, c: s.count(c) if len(s)>10 else 'String is too short.'