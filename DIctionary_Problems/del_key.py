"""
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title: Remove Key from Dictionary
"""


def remove_key_from_dict(my_dict, key_to_remove):
    
    
    """
    Removes a key from the dictionary if it exists.
    
    Parameters:
        my_dict (dict): The dictionary from which to remove the key.
        key_to_remove (str or int): The key to be removed from the dictionary.
        
    Returns:
        dict: The updated dictionary after removing the key, or the original dictionary if the key does not exist.
    """
    
    
    try:
        if key_to_remove in my_dict:
            del my_dict[key_to_remove]
            print(f"Key '{key_to_remove}' has been removed.")
        else:
            print(f"Key '{key_to_remove}' not found in the dictionary.")
        return my_dict
    except Exception as e:
        print(f"An error occurred: {e}")
        return my_dict



def main():
    try:
        # Sample dictionary for demonstration
        sample_dict = {
            "name": "Alice",
            "age": 25,
            "city": "New York",
            "email": "alice@example.com"
        }
        
        print(f"Original dictionary: {sample_dict}")
        
        key_to_remove = input("Enter the key to remove from the dictionary: ")
        
        updated_dict = remove_key_from_dict(sample_dict, key_to_remove)
        print(f"Updated dictionary: {updated_dict}")
    
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
