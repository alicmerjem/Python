def checkElementInTuple(tpl, element):
    try:
        if not all(isinstance(i, tuple) for i in tpl):
            raise TypeError("Input is not a tuple of tuples")
        if not isinstance(element, str):
            raise TypeError("Element is not a string")
        return any(element in sub_tpl for sub_tpl in tpl)
    except TypeError as e:
        return f"Error: {str(e)}"

print(checkElementInTuple((('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime')), 'White'))  # True
print(checkElementInTuple((('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime')), 'Olive'))  # False
print(checkElementInTuple([], 'White'))  # 'Error: Input is not a tuple of tuples'
print(checkElementInTuple((('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple')), 5))  # 'Error: Element is not a string'
