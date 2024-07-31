

"""
@Author: Girish
@Date: 2024-07-24 
@Last Modified by: Girish
@Last Modified time: 2024-07-24 
@Title: Finding day of a week for given date
"""

import calendar

def print_calendar(month, year):
    """
    Prints the calendar for a given month and year.

    Parameters:
        month (int): The month to display (1 for January, 2 for February, ..., 12 for December).
        year (int): The year to display.

    Returns:
        None

    
    """
    try:
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12.")
        
        if year < 1:
            raise ValueError("Year must be a positive integer.")
        
        cal = calendar.TextCalendar(calendar.SUNDAY)
        month_calendar = cal.formatmonth(year, month)
        print(month_calendar)
    
    except ValueError as ve:
        print(f"Value Error: {ve}")

def main():
    
    
    """
    Main function to interact with the user and print the calendar for a specified month and year.

    This function prompts the user to enter a month and year, then calls the print_calendar function
    to display the calendar for the specified month and year.

    Returns:
        None

    
    """
    try:
        month = int(input("Enter the month (1-12): "))
        year = int(input("Enter the year (e.g., 2024): "))
        print_calendar(month, year)
    
    except ValueError:
        print("Invalid input. Please enter integers for month and year.")

if __name__ == '__main__':
    main()





