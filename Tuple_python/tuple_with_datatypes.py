'''
@Author: Girish
@Date: 2024-07-29
@Last Modified by: Girish
@Last Modified time: 2024-07-29
@Title : Tuple with Different Data Types
'''

def create_tuple_with_varied_types():
    
    
    """
    Description:
        Creates a tuple with elements of different data types.
    Parameters:
        None
    Returns:
        tuple: A tuple containing elements of various data types.
    """
    
    
    return (1, 2, 3.04, 6.5, "Bridge", "labs", True)



def main():
    try:
        variable = create_tuple_with_varied_types()
        print(f'Tuple with different data types: {variable}')
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
