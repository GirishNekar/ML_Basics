

'''
@Author: Girish
@Date: 2024-07-29
@Last Modified by: Girish
@Last Modified time: 2024-07-29
@Title: Search for an Element in a Tuple
'''


def is_element_in_list(my_list, element):
    
    
    """
    Description:
        Checks if a given element is present in the provided list.
    
    Parameters:
        my_list (list): The list to be checked.
        element (int): The element to search for in the list.
    
    Returns:
        bool: True if the element is found, False otherwise.
    """
    
    
    for number in my_list:
        if number == element:
            return True
    return False


def main():

    try:
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        element_to_find = int(input("Enter the number to find in the list: "))
        
        if is_element_in_list(my_list, element_to_find):
            print("True")
        else:
            print("False")
    
    except ValueError:
        print("Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")





if __name__ == "__main__":
    main()
