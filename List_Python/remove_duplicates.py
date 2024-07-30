'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Remove Duplicates from a List Without Inbuilt Functions
'''



def remove_duplicates(input_list):
    
    
    """
    Description:
        Removes duplicates from a list by iterating through the list and adding items to a new list only if they are not already present.
        
    Parameters:
        input_list (list): The list from which duplicates need to be removed.
        
    Returns:
        list: A new list with duplicates removed.
    """
    
    
    unique_list = []
    
    for item in input_list:
        found = False
        for unique_item in unique_list:
            if item == unique_item:
                found = True
                break
        
        if not found:
            unique_list.append(item)
    
    return unique_list



def main():
    
    
    try:
        input_list = []
        length = int(input("Enter the number of elements in the list: "))
        if length <= 0:
            raise ValueError("The number of elements must be a positive integer.")

        for index in range(length):
            item = input(f"Enter element {index + 1}: ")
            try:
                item = int(item)
            except ValueError:
                pass
            input_list.append(item)

        result_list = remove_duplicates(input_list)
        print("List after removing duplicates:", result_list)
    
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
