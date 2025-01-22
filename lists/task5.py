"""
two lists, return true if they have at
least one common element
"""
def common_member(lst1, lst2):
    for item in lst1:
        if item in lst2:
            return True
    return False