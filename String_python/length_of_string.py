'''
@Author: Girish
@Date: 2024-07-26
@Last Modified by: Girish
@Last Modified time: 2024-07-26
@Title : Calculate Length of a String Without Using Built-in Functions
'''



def length_of_string(string):
    
    
    """
    Description:
        Calculates the length of a given string without using built-in functions.
        
    Parameters:
        string (str): The input string for which the length is to be calculated.
        
    Returns:
        int: The length of the input string.
    """
    
    
    length = 0
    
    for char in string:
        length += 1
    
    return length

def main():
    
    
    
    """
    Description:
        Prompts the user to enter a string and then calculates and prints its length
        using the `length_of_string` function.
        
    Parameters:
        None
        
    Returns:
        None
    """
    
    
    
    string = input("Enter the String: ")
    
    print(f'Length of string is: {length_of_string(string)}')




if __name__ == "__main__":
    main()
    
    
    
    
    
