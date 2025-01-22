"""
Write a function that calculates 
hotel costs with arguments for nights, 
price, and guests. Hotel cost is 
calculated using the formula 
(nights*price)*guests. The price 
per night is 25$, and the user 
will input the number of nights and 
guests.
"""

def hotel_cost(nights, price, guests):
    price = 25
    cost = nights * price * guests
    return cost

nights = int(input("Enter the number of nights: "))
guests = int(input("enter the number of guests: "))

total = hotel_cost(nights, 25, guests)
print(total)

