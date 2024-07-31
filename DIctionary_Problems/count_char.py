"""
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title: Create Dictionary from String
"""


def count_characters(input_string):
    
    
    """
    Creates a dictionary with the count of each character in the input string.
    
    Parameters:
        input_string (str): The string from which to count characters.
        
    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    
    char_count = {}
    try:
        for char in input_string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    except Exception as e:
        print(f"An error occurred: {e}")
    return char_count



def main():
    try:
        sample_string = input("Enter a string: ")
        print(f"Input string: '{sample_string}'")
        
        character_count = count_characters(sample_string)
        print(f"Character count dictionary: {character_count}")
    
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
