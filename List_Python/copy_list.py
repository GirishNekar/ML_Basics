'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Clone or Copy a List
'''



def clone_list(input_list):
    """
    Description:
        Creates a copy of the provided list using slicing.
        
    Parameters:
        input_list (list): The list to be copied.
        
    Returns:
        list: A new list that is a copy of the input_list.
    """
    return input_list[:]



def main():
    try:
        length = int(input("Enter the number of elements in the list: "))
        if length <= 0:
            raise ValueError("The number of elements must be a positive integer.")
        input_list = []
        for index in range(length):
            item = input(f"Enter element {index + 1}: ")
            item = int(item)          
            input_list.append(item)
        cloned_list = clone_list(input_list)
        print("Original list:", input_list)
        print("Cloned list:", cloned_list)
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
