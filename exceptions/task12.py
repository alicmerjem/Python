def sumTupleElements(lst):
    try:
        if not lst:
            raise ValueError("List is empty")
        result = []
        for tpl in lst:
            if not all(isinstance(i, (int, float)) for i in tpl):
                raise ValueError("Non-numeric values found in tuple")
            result.append(sum(tpl))
        return result
    except ValueError as e:
        return f"Error: {str(e)}"

print(sumTupleElements([(1, 2), (2, 3), (3, 4)]))  # [3, 5, 7]
print(sumTupleElements([(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]))  # [9, -1, 7, 8]
print(sumTupleElements([]))  # 'Error: List is empty'
print(sumTupleElements([(1, 2), ('a', 3), (3, 4)]))  # 'Error: Non-numeric values found in tuple'
