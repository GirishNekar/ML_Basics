"""
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title: Count Number of Items in Dictionary Values that are Lists
"""



def count_items_in_list_values(dictionary):
    
    
    """
    Counts the number of items in dictionary values that are lists.
    
    Parameters:
        dictionary (dict): The dictionary to process.
        
    Returns:
        int: Total number of items in all list-type values in the dictionary.
    """
    
    
    total_count = 0
    for value in dictionary.values():
        if isinstance(value, list):
            total_count += len(value)
    return total_count



def main():
    try:
        
        sample_dict = {
            'fruits': ['apple', 'banana', 'cherry'],
            'numbers': [1, 2, 3, 4, 5],
            'colors': ['red', 'blue'],
            'name': 'Girish' 
        }

      
        total_items = count_items_in_list_values(sample_dict)
        print(f"Total number of items in list-type values: {total_items}")

    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
