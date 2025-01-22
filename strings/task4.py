"""
occcurence of xyz - question bank
"""

def contains_xyz(string):
    for i in range(len(str) - 2):
        if string[i:i+3] == 'xyz':
            if i == 0 or string[i-1] != '.':
                return True
            return False
        
    
print(contains_xyz('aaabcxyz'))
print(contains_xyz('x.xyz'))