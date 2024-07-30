'''
@Author: Girish
@Date: 2024-07-26
@Last Modified by: Girish
@Last Modified time: 2024-07-26
@Title : Remove First Occurrence of a Specified Element from an Array Using array Module
'''

import array

def remove_first_occurrence(arr, element):
    
    
    """
    Description:
        Removes the first occurrence of the specified element from the provided array.
        If the element is not found, the array remains unchanged.
        
    Parameters:
        arr (array.array): The array of integers.
        element (int): The element to remove.
        
    Returns:
        array.array: The updated array after removal of the specified element.
    """
    
    
    try:
        index = arr.index(element)
        arr = array.array('i', [arr[i] for i in range(len(arr)) if i != index])
    except ValueError:
        print(f"Element {element} not found in the array.")
    return arr

def main():

    arr = array.array('i')  
    
    try:
        length = int(input("Enter the length of the array to be created: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the length.")
        return

    for iterator in range(length):
        try:
            x = int(input(f"Enter number {iterator + 1}: "))
            arr.append(x)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return
    
    try:
        element = int(input("Enter the element to remove its first occurrence: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    updated_array = remove_first_occurrence(arr, element)
    print(f"Updated array after removing the first occurrence of {element}:\n", list(updated_array))

if __name__ == "__main__":
    main()
