def replaceChars(input_str):
    try:
        if not isinstance(input_str, str):
            raise TypeError("Input must be a string")
        if len(input_str) > 1:
            first_char = input_str[0]
            return first_char + input_str[1:].replace(first_char, '$')
        return input_str
    except TypeError as e:
        return f"Error: {str(e)}"

print(replaceChars('restart'))  # 'resta$t'
print(replaceChars('ehello'))   # 'eh$llo'
print(replaceChars(12345))      # 'Error: Input must be a string'
