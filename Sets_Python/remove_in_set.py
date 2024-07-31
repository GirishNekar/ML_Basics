'''

@Author: Girish
@Date: 2024-07-30 
@Last Modified by: Girish
@Last Modified time: 2024-07-30 
@Title : Remove Element from Set

'''



def remove_element(element_to_remove, initial_set):
    
    
    """
    Description:
        Removes an element from the provided set.
        
    Parameters:
        element_to_remove (int): The element to be removed from the set.
        initial_set (set): The set from which the element will be removed.
        
    Returns:
        set: The updated set with the element removed.
    """
    
    
    
    try:
        initial_set.remove(element_to_remove)
    except KeyError:
        print(f"The element {element_to_remove} is not in the set.")
    return initial_set



def main():
    try:
        initial_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        print("Initial set:", initial_set)
        element_to_remove = int(input("Enter the element to remove: "))
        new_set = remove_element(element_to_remove, initial_set)
        print(f"New set after removal of the element: {new_set}")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
