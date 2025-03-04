def days_in_month():
    """
    This function takes month and year as input from the user and prints the number of days in that month.
    """
    try:
        month = int(input("Enter the month (1-12): "))
        
        if month < 1 or month > 12:
            print("Invalid month. Please enter a month between 1 and 12.")
            return

        if month in (1, 3, 5, 7, 8, 10, 12):
            days = 31
            
        elif month == 2:
            year = int(input("Enter the year: "))
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                days = 29  # Leap year
            else:
                days = 28
        else:
            days = 30

        print(f"Number of days in {month}: {days}")

    except ValueError:
        print("Invalid input. Please enter valid integers for month and year.")

# Call the function to execute the program
days_in_month()