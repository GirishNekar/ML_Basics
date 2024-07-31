'''
@Author: Girish
@Date: 2024-07-26
@Last Modified by: Girish
@Last Modified time: 2024-07-26
@Title : Replace Subsequent Occurrences of the First Character in a String
'''

def change_first_char(string):
    
    
    """
    Description:
        Replaces all occurrences of the first character in the string (except the first character itself) with a '$' character.
        
    Parameters:
        string (str): The input string to modify.
        
    Returns:
        str: The modified string with subsequent occurrences of the first character replaced by '$'.
    """
    
    
    if not string:
        return "The string is empty."
    
    first_char = string[0]
    new_string = first_char
    
    for char in string[1:]: 
        if char == first_char:
            new_string += '$'
        else:
            new_string += char
            
    return new_string



def main():

    try:
        string = input("Enter the string: ").strip()
        if not string:
            raise ValueError("The string cannot be empty.")
        print("Modified string:", change_first_char(string))
    except ValueError as e:
        print(e)



if __name__ == "__main__":
    main()
