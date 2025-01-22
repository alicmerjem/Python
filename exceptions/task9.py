def combineListsToDict(list1, list2):
    try:
        if len(list1) != len(list2):
            raise ValueError("Lists have different lengths")
        if not list1:
            raise ValueError("First list is empty")
        if not list2:
            raise ValueError("Second list is empty")
        if not all(isinstance(i, int) for i in list2):
            raise ValueError("Second list must contain only integers")
        if len(set(list1)) != len(list1):
            raise ValueError("First list must contain unique values")

        return {list1[i]: list2[i] + list2[i+1] if i+1 < len(list2) else list2[i] for i in range(len(list1))}
    except ValueError as e:
        return f"Error: {str(e)}"

print(combineListsToDict(['a', 'b', 'c'], [1, 2, 3, 4]))  # {'a': 3, 'b': 5, 'c': 7}
print(combineListsToDict(['a', 'b', 'c', 'a'], [1, 2, 3]))  # 'Error: Lists have different lengths'
print(combineListsToDict([], [1, 2, 3]))  # 'Error: First list is empty'
print(combineListsToDict(['a', 'b'], []))  # 'Error: Second list is empty'
