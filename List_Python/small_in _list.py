'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Get the Smallest Number from a List with Exception Handling
'''

def find_smallest_number(items_list):
    
    
    """
    Description:
        Finds the smallest number in the provided list.
        
    Parameters:
        items_list (list): The list of integers.
        
    Returns:
        int: The smallest number in the list.
    """
    
    
    if not items_list:
        raise ValueError("The list is empty.")
        
    smallest = items_list[0]
    for item in items_list:
        if item < smallest:
            smallest = item
    return smallest




def main():
    try:
        length = int(input("Enter the number of items in the list: "))
        if length <= 0:
            raise ValueError("The number of items must be a positive integer.")

        items_list = []
        for i in range(length):
            item = int(input(f"Enter item {i + 1}: "))
            items_list.append(item)
        
        smallest_number = find_smallest_number(items_list)
        print(f"The smallest number in the list is: {smallest_number}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
