'''
@Author: Girish
@Date: 2024-07-26
@Last Modified by: Girish
@Last Modified time: 2024-07-26
@Title : Complete a String Based on Given Incomplete String with Exception Handling
'''

def complete_string(incomplete_string, full_string, len_of_incomplete_string):
    
    
    """
    Description:
        Completes the string by appending the remaining part of the full string
        to the given incomplete string.
        
    Parameters:
        incomplete_string (str): The string to be completed.
        full_string (str): The full string from which the remainder is appended.
        len_of_incomplete_string (int): The length of the incomplete string.
        
    Returns:
        None
    """
    
    
    next_string = full_string[len_of_incomplete_string:]
    completed_string = incomplete_string + next_string
    print("Completed string:", completed_string)

def main():

    try:
        full_string = input("Enter the full string: ").strip()
        incomplete_string = input("Enter the incomplete string: ").strip()
        
        if not full_string or not incomplete_string:
            raise ValueError("Both the full string and the incomplete string must be non-empty.")
        
        len_of_incomplete_string = len(incomplete_string)
        
        if full_string.startswith(incomplete_string):
            complete_string(incomplete_string, full_string, len_of_incomplete_string)
        else:
            print("Incorrect incomplete string.")
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
