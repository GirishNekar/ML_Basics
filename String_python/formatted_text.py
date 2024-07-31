'''
@Author: Girish
@Date: 2024-07-26
@Last Modified by: Girish
@Last Modified time: 2024-07-26
@Title : Format Text with Exception Handling and Text Size Adjustment
'''


def formatted_text(first_name, last_name, text_size):
    
    
    """
    Description:
        Formats the input first name and last name into a descriptive string.
        Adjusts the size of the last name to a specific width if specified.
        
    Parameters:
        first_name (str): The first name to include in the message.
        last_name (str): The last name to include in the message, with optional formatting.
        text_size (int, optional): The size to set for the last name, default is 40.
        
    Returns:
        str: The formatted string with the last name adjusted to the specified text size.
    """
    
    
    if text_size < 1:
        raise ValueError("Text size must be a positive integer.")
    
    last_name_formatted = last_name.ljust(text_size)
    return f'Your First Name is {first_name} and your Last Name is {last_name_formatted}'



def main():
    
    try:
        first_name = input("Enter your first name: ").strip()
        last_name = input("Enter your last name: ").strip()
        
        if not first_name or not last_name:
            raise ValueError("Both first name and last name must be provided.")
        
        # Set the text size for the last name
        text_size = 40
        
        print(formatted_text(first_name, last_name, text_size))
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




if __name__ == "__main__":
    main()
