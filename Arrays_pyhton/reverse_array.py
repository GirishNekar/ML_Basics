'''
@Author: Girish
@Date: 2024-07-26
@Last Modified by: Girish
@Last Modified time: 2024-07-26
@Title : Reverse an Array Using array Module
'''

import array

def create_and_reverse_array():
    """
    Description:
        Prompts the user to enter the length of an array and its elements.
        Validates the inputs and raises an exception if a number is less than or equal to 0.
        Reverses the array and prints it.
        
    Parameters:
        None
        
    Returns:
        None
    """
    arr = array.array('i')  # Create an array of integers ('i' typecode for signed integer)
    
    try:
        length = int(input("Enter the length of the array to be created: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the length.")
        return

    for index in range(length):
        while True:
            try:
                x = int(input(f"Enter number {index + 1}: "))
                if x <= 0:
                    raise ValueError("Number cannot be less than or equal to 0")
                arr.append(x)
                break
            except ValueError as e:
                print(e)
    
    reversed_array = arr[::-1]  # Reverse the array
    print("Reversed array:", reversed_array.tolist())  # Convert array to list for easy printing

def main():
    create_and_reverse_array()

if __name__ == "__main__":
    main()
