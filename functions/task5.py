"""
forbidden range - question bank
"""
def sorta_sum(a, b):
    total = a + b
    # Return 20 if sum is in the forbidden range
    if 10 <= total <= 19:
        return 20
    return total

# Test cases
print(sorta_sum(3, 4))   # → 7
print(sorta_sum(9, 4))   # → 20
print(sorta_sum(10, 11)) # → 21
