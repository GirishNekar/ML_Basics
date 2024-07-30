"""
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title: Convert List into Nested Dictionary
"""


def list_to_nested_dict(lst):
    
    
    """
    Converts a list into a nested dictionary of keys.
    
    Parameters:
        lst (list): A list of elements to be converted into a nested dictionary.
        
    Returns:
        dict: A nested dictionary created from the list.
    """
    
    
    nested_dict = current = {}
    for item in lst:
        current[item] = {}
        current = current[item]
    return nested_dict



def main():
    try:
        input_list = input("Enter elements of the list separated by space: ").split()
        nested_dict = list_to_nested_dict(input_list)
        print("Nested dictionary:", nested_dict)
    
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
