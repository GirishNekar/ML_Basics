

'''
@Author: Girish
@Date: 2024-07-29
@Last Modified by: Girish
@Last Modified time: 2024-07-29
@Title: Search for an Element in a Tuple
'''


def create_tuple_from_list(my_list):
    
    
    """
    Description:
        Converts a list into a tuple.
    
    Parameters:
        my_list (list): The list to be converted into a tuple.
    
    Returns:
        tuple: A tuple created from the provided list.
    """
    
    
    return tuple(my_list)


def main():

    try:
        my_list = [1, 2, 3, 4, "Girish", 0.02]
        created_tuple = create_tuple_from_list(my_list)
        
        print(f'List: {my_list}')
        print(f'Tuple: {created_tuple}')
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
