'''
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title : Sort Dictionary by Value
'''


def concatenate_dicts(dict1, dict2):
    
    
    """
    Concatenate two dictionaries. If there are overlapping keys,
    values from the second dictionary will overwrite those from the first.
    
    Parameters:
    dict1 (dict): The first dictionary.
    dict2 (dict): The second dictionary.
    
    Returns:
    dict: A new dictionary with keys and values from both dictionaries.
    """

    result_dict = dict1.copy()
    
    
    for key, value in dict2.items():
        result_dict[key] = value
    
    return result_dict



def main():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    
    merged_dict = concatenate_dicts(dict1, dict2)
    
    print("Merged Dictionary:", merged_dict)



if __name__ == "__main__":
    main()
