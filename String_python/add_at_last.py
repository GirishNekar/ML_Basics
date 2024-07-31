'''
@Author: Girish
@Date: 2024-07-26
@Last Modified by: Girish
@Last Modified time: 2024-07-26
@Title : String Suffix Modification with Exception Handling
'''

def add_ly(string):
    
    
    
    """
    Description:
        Adds the suffix 'ly' to the given string.
        
    Parameters:
        string (str): The input string to modify.
        
    Returns:
        str: The modified string with 'ly' appended.
    """
    
    
    return string + 'ly'

def add_ing(string):
    
    
    """
    Description:
        Adds the suffix 'ing' to the given string.
        
    Parameters:
        string (str): The input string to modify.
        
    Returns:
        str: The modified string with 'ing' appended.
    """
    
    
    return string + 'ing'

def modify_string_suffix(string):
    
    
    """
    Description:
        Modifies the string based on its length and suffix. Adds 'ing' if the string does not end with 'ing',
        otherwise adds 'ly'. Also checks for very small strings.
        
    Parameters:
        string (str): The input string to analyze and modify.
        
    Returns:
        str: The modified string.
    """
    
    
    if len(string) < 3:
        return "Very Small String"
    elif string[-3:] != 'ing':
        return add_ing(string)
    else:
        return add_ly(string)



def main():

    try:
        string = input("Enter the string: ").strip()
        if not string:
            raise ValueError("The string cannot be empty.")
        print(modify_string_suffix(string))
    except ValueError as e:
        print(e)



if __name__ == "__main__":
    main()
