"""
write a function to check if a word 
is a palindrome
"""
def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False
