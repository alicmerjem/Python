def tupleToInt(tpl):
    try:
        if not tpl:
            raise ValueError("Tuple is empty")
        if not all(isinstance(i, int) and i > 0 for i in tpl):
            raise ValueError("Tuple contains non-positive integers")
        return int(''.join(map(str, tpl)))
    except ValueError as e:
        return f"Error: {str(e)}"

print(tupleToInt((1, 2, 3)))  # 123
print(tupleToInt((10, 20, 40, 5, 70)))  # 102040570
print(tupleToInt((1, -2, 3)))  # 'Error: Tuple contains non-positive integers'
print(tupleToInt(()))  # 'Error: Tuple is empty'
