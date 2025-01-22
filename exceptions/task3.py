def convertToInt(string):
    try:
        result = int(string)
    except ValueError: 
        return 'Error: cannot convert string to integer'
    else:
        return 'conversion successfull'