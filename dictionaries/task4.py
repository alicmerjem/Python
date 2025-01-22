"""
matching key value pairs in two
dicts and printing whether the key
and value exist in both
"""
def matchKeys(d1, d2):
    for key, value in d1.items():
        if key in d2 and d2[key] == value:
            print("The value is present in both dictionaries")
    