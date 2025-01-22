"""
sum numbers from 1 to n
"""
def sum_up(n):
    if n<=1:
        return
    return n + sum_up(n-1)
