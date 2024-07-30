'''
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title : Sort Dictionary by Value
'''


def sort_dict_by_value(d, reverse=False):
    
    
    """
    Description:
        Sorts a dictionary by its values.
        
    Parameters:
        d (dict): The dictionary to be sorted.
        reverse (bool): If True, sorts the dictionary in descending order. Defaults to False (ascending order).
        
    Returns:
        dict: A new dictionary sorted by values.
        
    """
    
    
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))
    return sorted_dict



def main():

    try:
        my_dict = {
            'apple': 10,
            'banana': 5,
            'cherry': 7,
            'date': 12
        }

        print("Original dictionary:", my_dict)
        
        ascending_sorted_dict = sort_dict_by_value(my_dict)
        print("Dictionary sorted by value in ascending order:")
        for key, value in ascending_sorted_dict.items():
            print(f"{key}: {value}")

        descending_sorted_dict = sort_dict_by_value(my_dict, reverse=True)
        print("Dictionary sorted by value in descending order:")
        for key, value in descending_sorted_dict.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
