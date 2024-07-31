'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Reverse a String with Exception Handling
'''

def reverse_string(user_string):
    
    
    """
    Description:
        Reverses the given string.
        
    Parameters:
        user_string (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    
    
    return user_string[::-1]



def main():

    try:
        user_string = input("Enter the string to be reversed: ")
        
      
        if len(user_string) == 0:
            raise ValueError("The string must be non-empty.")
        
        reversed_str = reverse_string(user_string)
        print(f"Reversed string: {reversed_str}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    main()
