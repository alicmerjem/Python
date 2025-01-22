"""
count backwards by 2
"""
def count_backwards(n):
    if n<0:
        return
    print(n)
    count_backwards(n-2)