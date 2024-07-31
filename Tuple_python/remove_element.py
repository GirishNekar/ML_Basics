

'''
@Author: Girish
@Date: 2024-07-29
@Last Modified by: Girish
@Last Modified time: 2024-07-29
@Title : Create Tuple from List
'''


def remove_element_from_list(lst, element):
    
    
    """
    Description:
        Removes the first occurrence of the specified element from the list.
    
    Parameters:
        lst (list): The list from which the element is to be removed.
        element: The element to remove from the list.
    
    Returns:
        list: A new list with the specified element removed.
    """
    
    
    new_list = []
    found = False
    for item in lst:
        if item == element and not found:
            found = True
        else:
            new_list.append(item)
    return new_list


def main():

    try:
        my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
        print(f'Original tuple: {my_tuple}')
        
        list_1 = list(my_tuple)
        
        remove_element = int(input("Enter the element to remove: "))
        
        updated_list = remove_element_from_list(list_1, remove_element)
        
        new_tuple = tuple(updated_list)
        print(f'Updated tuple: {new_tuple}')
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
