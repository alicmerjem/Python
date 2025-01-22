"""
set number to the power using 
recursion
"""
def power(num, topw):
    if topw == 0:
        return 1
    else:
        return num * power(num, topw - 1)
    