'''
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title : Add Key-Value Pair to Dictionary
'''


def add_key_to_dict(d, key, value):
    
    
    """
    Description:
        Adds a key-value pair to the dictionary.
        
    Parameters:
        d (dict): The dictionary to which the key-value pair will be added.
        key: The key to be added.
        value: The value associated with the key.
        
    Returns:
        dict: The updated dictionary.
        
    """
    
    
    d[key] = value
    return d




def main():

    try:
        my_dict = {
            'apple': 10,
            'banana': 5,
            'cherry': 7
        }

        print("Original dictionary:", my_dict)

        key = input("Enter the key to add: ")
        value = input("Enter the value to add: ")


        my_dict = add_key_to_dict(my_dict, key, value)

        print("Updated dictionary:", my_dict)

    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
