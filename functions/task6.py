"""
making bricks - question bank
"""

def make_bricks(small, big, goal):
    # Use as many big bricks as possible without exceeding the goal
    max_big = min(goal // 5, big)
    remaining_goal = goal - (max_big * 5)
    
    # Check if the remaining goal can be met with small bricks
    return remaining_goal <= small

# Test cases
print(make_bricks(3, 1, 8))   # → True
print(make_bricks(3, 1, 9))   # → False
print(make_bricks(3, 2, 10))  # → True
