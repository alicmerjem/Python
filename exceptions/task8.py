def checkKey(d, key):
    try:
        if not d:
            raise KeyError("Dictionary is empty")
        if key in d:
            return 'Key exists'
        else:
            return 'Key does not exist'
    except KeyError as e:
        return f"Error: {str(e)}"

print(checkKey({'name': 'Alice', 'age': 25}, 'age'))  # 'Key exists'
print(checkKey({'name': 'Alice', 'age': 25}, 'address'))  # 'Key does not exist'
print(checkKey({}, 'name'))  # 'Error: Dictionary is empty'
