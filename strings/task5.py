"""
write a function to return how many
times the string code appears anywhere
in the given string, except we will
accept any letter for the d, so cope
is fine and cooe as well
"""

def count_code_variants(code):
    count = 0
    for i in range(len(code)-3):
        if code[i] == 'c':
            if code[i+1] == 'o':
                if code[i+3] == 'e':
                    count +=1
    return count