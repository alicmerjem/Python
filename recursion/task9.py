"""
printing even numbers in range 
from start to end
"""

def print_in_range(start, end):
    if start>end:
        return
    
    if start%2!=0:
        start+=1
    
    print(start)
    print_in_range(start+2, end)