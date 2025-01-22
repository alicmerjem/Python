def splitList(lst, length):
    try:
        if length < 0:
            raise ValueError("Invalid length")
        if not lst:
            raise ValueError("List is empty")
        if length > len(lst):
            raise ValueError("Length exceeds list size")
        return lst[:length], lst[length:]
    except ValueError as e:
        return f"Error: {str(e)}"

print(splitList([1, 1, 2, 3, 4, 4, 5, 1], 3))  # ([1, 1, 2], [3, 4, 4, 5, 1])
print(splitList([1, 1, 2, 3, 4, 4, 5, 1], 10)) # 'Error: Length exceeds list size'
print(splitList([1, 1, 2, 3, 4, 4, 5, 1], -2))  # 'Error: Invalid length'
print(splitList([], 2))  # 'Error: List is empty'
