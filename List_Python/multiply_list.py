'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Multiply All Items in a List with Exception Handling
'''

def multiply_list(items_list):
    
    
    """
    Description:
        Multiplies all the items in the provided list.
        
    Parameters:
        items_list (list): The list of integers to be multiplied.
        
    Returns:
        int: The product of all items in the list.
    """
    
    
    product = 1
    for item in items_list:
        product *= item
    return product



def main():
    try:
        length = int(input("Enter the number of items in the list: "))
        if length <= 0:
            raise ValueError("The number of items must be a positive integer.")

        items_list = []
        for i in range(length):
            
                item = int(input(f"Enter item {i + 1}: "))
                items_list.append(item)
        total_product = multiply_list(items_list)
        print(f"The product of all items in the list is: {total_product}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
