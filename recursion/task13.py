"""
find numbers divisible by 3 and 5 in the
given range
"""
def divisble_3_5(start, end):
    if start>end:
        return
    
    if start%3==0 and start%5==0:
        print(start)
    
    print(divisble_3_5(start+1, end))