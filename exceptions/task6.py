def findItemIndex(lst, item):
    try:
        return lst.index(item)
    except ValueError:
        return 'Item not found in the list'

print(findItemIndex([1, 2, 3, 4, 5], 3))  # 2
print(findItemIndex([1, 2, 3, 4, 5], 6))  # 'Item not found in the list'
print(findItemIndex([], 3))  # 'Item not found in the list'
