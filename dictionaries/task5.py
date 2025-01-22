"""
removing spaces from dict keys
"""

def removeSpaces(d):
    return {key.replace(" ", ''): value for key, value in d.items()}
