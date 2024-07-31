

'''
@Author: Girish
@Date: 2024-07-26
@Last Modified by: Girish
@Last Modified time: 2024-07-26
@Title : Frequency of Characters in a String with Exception Handling
'''

def frequency_of_char(string):
    
    
    """
    Description:
        Calculates the frequency of each character in the provided string.
        
    Parameters:
        string (str): The input string to analyze.
        
    Returns:
        dict: A dictionary with characters as keys and their frequencies as values.
    """
    
    
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency



def main():



    try:
        string = input("Enter the string: ")
        if not string:  # Check if the input is empty
            raise ValueError("String cannot be empty.")
        freq = frequency_of_char(string)
        print("Frequency of characters:", freq)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    main()
