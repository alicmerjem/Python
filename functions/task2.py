"""
Ask the user to enter a number. 
If the user enters a number larger 
than 1000, the digits should be 
subtracted from one another from 
right to left (ex. 2159 -> 9-5-1-2). 
If the number is smaller than 1000, 
then the digits should be added 
(ex. 125 -> 1+2+5) Result should be 
returned to the place where the function 
was called. If a user enters a zero 
or negative number, immediately exit 
the program. 
"""

def process_number():
    # Ask the user for input
    num = int(input("Enter a number: "))
    
    # Check if the number is zero or negative
    if num <= 0:
        print("Program exited.")
        exit()
    
    # Convert the number to a string to work with individual digits
    num_str = str(num)
    
    # Initialize result based on the condition
    if num > 1000:
        # Start with the rightmost digit and subtract
        result = int(num_str[-1])  # Start with the last digit
        for digit in reversed(num_str[:-1]):  # Iterate through the rest of the digits
            result -= int(digit)
    else:
        # Add the digits for numbers smaller than 1000
        result = sum(int(digit) for digit in num_str)
    
    return result


# Call the function and display the result
result = process_number()
print("The result is:", result)
