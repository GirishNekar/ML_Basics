'''
@Author: Girish
@Date: 2024-07-26
@Last Modified by: Girish
@Last Modified time: 2024-07-26
@Title : Integer Array Input and Index Access with Exception Handling Using array Module
'''

import array

def get_integer_array(size):
    """
    Description:
        Prompts the user to enter integer values, which are stored in an array.
        
    Parameters:
        size (int): The number of integers to be added to the array.
        
    Returns:
        array.array: The array of integers.
    """
    arr = array.array('i')  # Create an array of integers ('i' typecode for signed integer)
    
    for index in range(size):
        while True:
            try:
                x = int(input(f"Please enter number {index + 1}: "))
                arr.append(x)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    
    return arr


def access_element(arr):
    """
    Description:
        Prompts the user for an index to access and prints the element at that index.
        Handles exceptions for invalid integer inputs and out-of-range indices.
        
    Parameters:
        arr (array.array): The array of integers.
        
    Returns:
        None
    """
    try:
        ind = int(input("Enter the index value to access: "))
        if ind < 0 or ind >= len(arr):
            print("Index out of range.")
        else:
            print("Element at index", ind, "is", arr[ind])
    except ValueError:
        print("Invalid input. Please enter a valid integer for the index.")
    except IndexError:
        print("Index out of range.")

def main():

    arr = get_integer_array(5)
    print("Array:", arr.tolist())  # Convert array to list for easy printing
    access_element(arr)

if __name__ == "__main__":
    main()
