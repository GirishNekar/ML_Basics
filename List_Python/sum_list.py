'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Sum All Items in a List with Exception Handling
'''


def sum_of_list(items_list):
    
    
    """
    Description:
        Sums all the items in the provided list.
        
    Parameters:
        items_list (list): The list of integers to be summed.
        
    Returns:
        int: The sum of all items in the list.
    """
    
    
    total = 0
    for item in items_list:
        total += item
    return total



def main():
    try:
        length = int(input("Enter the number of items in the list: "))
        if length <= 0:
            raise ValueError("The number of items must be a positive integer.")

        items_list = []
        for number in range(length):
            
                item = int(input(f"Enter item {number + 1}: "))
                items_list.append(item)
        total_sum = sum_of_list(items_list)
        print(f"The sum of all items in the list is: {total_sum}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    main()
