'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Count Occurrences of a Substring in a String with Exception Handling
'''


def count_substring_occurrences(main_string, substring):
    
    
    """
    Description:
        Counts the occurrences of a specified substring within the main string
        using a custom method without built-in functions.
        
    Parameters:
        main_string (str): The string in which to search for the substring.
        substring (str): The substring to count occurrences of.
        
    Returns:
        int: The number of occurrences of the specified substring in the main string.
    """
    
    
    count = 0
    sub_len = len(substring)
    main_len = len(main_string)
    
    for i in range(main_len - sub_len + 1):
        if main_string[i:i+sub_len] == substring:
            count += 1
    return count



def main():



    try:
        main_string = input("Enter the main string: ")
        substring = input("Enter the substring to count: ")
        
        if len(main_string) == 0 or len(substring) == 0:
            raise ValueError("Both the main string and the substring must be non-empty.")
        
        occurrences = count_substring_occurrences(main_string, substring)
        print(f"The substring '{substring}' occurs {occurrences} time(s) in the main string.")
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    main()
