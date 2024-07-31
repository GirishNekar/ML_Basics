"""
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title: Check Multiple Keys Existence in a Dictionary
"""


def check_multiple_keys_existence(dictionary, keys):
    
    
    """
    Checks if all specified keys exist in the given dictionary.
    
    Parameters:
        dictionary (dict): The dictionary to check.
        keys (list): The list of keys to check for existence in the dictionary.
        
    Returns:
        bool: True if all specified keys are present in the dictionary, False otherwise.
    """
    
    
    for key in keys:
        if key not in dictionary:
            return False
    return True



def main():
    try:
        
        sample_dict = {
            'name': 'Girish',
            'age': 30,
            'city': 'Bangalore',
            'profession': 'Developer'
        }

        
        keys_input = input("Enter the keys to check (separated by commas): ")
        keys_list = [key.strip() for key in keys_input.split(',')]

        
        if check_multiple_keys_existence(sample_dict, keys_list):
            print("All specified keys are present in the dictionary.")
        else:
            print("Not all specified keys are present in the dictionary.")
    
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
