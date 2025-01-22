"""
print found target and return a new
set with numbes greater than target
"""

def find_and_filter(s, target):
    if target in s:
        print("Found target.")
    new_set = {x for x in s if s>target}
    return new_set
