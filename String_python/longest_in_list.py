'''
@Author: Girish
@Date: 2024-07-26
@Last Modified by: Girish
@Last Modified time: 2024-07-26
@Title : Find the Length of the Longest Word in a List with Exception Handling
'''


def longest_in_list(string_list):
    
    
    """
    Description:
        Finds the length of the longest word in the provided list of strings.
        
    Parameters:
        string_list (list): A list of strings to analyze.
        
    Returns:
        int: The length of the longest word.
    """
    
    
    if not string_list:
        return "The list is empty."

    max_length = 0
    for word in string_list:
        if len(word) > max_length:
            max_length = len(word)
    
    return max_length

def main():

    try:
        string_list = []
        no_of_words = int(input("Enter the number of words: "))
        
        if no_of_words <= 0:
            raise ValueError("The number of words must be a positive integer.")
        
        for index in range(no_of_words):
            string = input(f'Enter word {index + 1}: ').strip()
            if not string:
                raise ValueError("Empty strings are not allowed.")
            string_list.append(string)

        result = longest_in_list(string_list)
        print("Length of the longest word:", result)
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
