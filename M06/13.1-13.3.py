'''
M06 Programing Assignment 13.1-13.3
April 23, 2024
Taylor Hickman
'''
from datetime import datetime

# Read the text file today.txt into the string today_string.
with open ("M06/today.txt", "r") as file:
    today_string = file.read()


# Parse the date from today_string.
parse_date = datetime.strptime(today_string)
print(parse_date)
