"""
write a lambda functiont to check the
temperature: 
hot if temp > 22
warm if temp  betwee 10 and 22
freezing if temp < 10
"""

temp = int(input("enter a temp: "))
temperature = lambda temp: 'hot' if temp>22 else ('warm' if temp>= 10 and temp<=23 else 'Freezing')