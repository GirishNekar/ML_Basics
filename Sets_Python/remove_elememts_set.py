'''

@Author: Girish
@Date: 2024-07-30 
@Last Modified by: Girish
@Last Modified time: 2024-07-30 
@Title : Remove Elements from Set

'''

def remove_element(initial_set):
    
    
    """
    Description:
        Removes an element from the provided set.
        
    Parameters:
        element_to_remove (int): The element to be removed from the set.
        initial_set (set): The set from which the element will be removed.
        
    Returns:
        set: The updated set with the elements removed.
    """
    
    for index in range(3):
        initial_set.pop()
    
    return initial_set



def main():
    
    initial_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    new_set = remove_element(initial_set)
    print(f"New set after removal of the element: {new_set}")
 
      

if __name__ == "__main__":
    main()
