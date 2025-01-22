"""
double numbers divisible by 3
"""
def divisible_3(tup):
    return tuple(x*2 if x%3==0 else x for x in tup)
