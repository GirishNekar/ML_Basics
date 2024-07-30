"""
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title: Count Values Associated with a Key in a List of Dictionaries
"""


def count_values(data_list, key):
    
    
    """
    Counts the number of dictionaries in the list that have the specified key with a True value.
    
    Parameters:
        data_list (list): A list of dictionaries.
        key (str): The key to look for in the dictionaries.
        
    Returns:
        int: The count of dictionaries with the key having the value True.
    """
    
    
    count = 0
    for dictionary in data_list:
        if dictionary.get(key) is True:
            count += 1
    return count



def main():
    try:
        sample_data = [
            {'id': 1, 'success': True, 'name': 'Lary'},
            {'id': 2, 'success': False, 'name': 'Rabi'},
            {'id': 3, 'success': True, 'name': 'Alex'}
        ]

        key_to_count = 'success'
        count = count_values(sample_data, key_to_count)
        print(f"Count of dictionaries with '{key_to_count}' key set to True: {count}")
    
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
