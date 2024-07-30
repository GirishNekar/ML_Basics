

'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Lowercase First n Characters in a String with Exception Handling
'''


def lowercase_first_n_chars(user_string, number):
    
    
    """
    Description:
        Converts the first n characters of the given string to lowercase.
        
    Parameters:
        user_string (str): The original string.
        n (int): The number of characters to convert to lowercase.
        
    Returns:
        str: The modified string with the first n characters in lowercase.
    """
    
    
    if number > len(user_string):
        raise ValueError("n cannot be greater than the length of the string.")
    
    return user_string[:number].lower() + user_string[number:]



def main():

    try:
        user_string = input("Enter the string: ")
        n = int(input("Enter the number of characters to lowercase: "))
        
        if n < 0:
            raise ValueError("The number of characters to lowercase must be a non-negative integer.")
        
        modified_string = lowercase_first_n_chars(user_string, n)
        print(f"String after lowercasing first {n} characters: {modified_string}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    main()
