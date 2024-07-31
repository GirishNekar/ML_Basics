'''
@Author: Girish
@Date: 2024-07-26
@Last Modified by: Girish
@Last Modified time: 2024-07-26
@Title : Convert String to Uppercase and Lowercase with Exception Handling
'''

def upper_case(user_string):
    
    
    """
    Description:
        Converts the given string to uppercase.
        
    Parameters:
        user_string (str): The input string to convert.
        
    Returns:
        str: The uppercase version of the input string.
    """
    
    
    return user_string.upper()

def lower_case(user_string):
    
    
    
    """
    Description:
        Converts the given string to lowercase.
        
    Parameters:
        user_string (str): The input string to convert.
        
    Returns:
        str: The lowercase version of the input string.
    """
    
    
    return user_string.lower()



def main():

    try:
        user_string = input("Enter the string: ").strip()
        if not user_string:
            raise ValueError("The string cannot be empty.")
        
        print("Uppercase:", upper_case(user_string))
        print("Lowercase:", lower_case(user_string))
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    main()
