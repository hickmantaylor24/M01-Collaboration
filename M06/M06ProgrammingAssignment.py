'''
M06 Programing Assignment
April 23, 2024
Taylor Hickman
'''
from datetime import datetime

'''
13.1 Write the current date as a string to the text file today.txt.

13.2 Read the text file today.txt into the string today_string.

13.3 Parse the date from today_string.
'''
with open ("M06/today.txt", "r") as file:
    today_string = file.read()

parse_date = datetime.strptime(today_string)
print(parse_date)
