'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Remove Duplicates from a List of Lists
'''

def remove_duplicates(list_of_lists):
    
    
    """
    Description:
        Removes duplicate sublists from a list of lists.
        
    Parameters:
        list_of_lists (list of lists): The list containing sublists to remove duplicates from.
        
    Returns:
        list of lists: A new list with duplicate sublists removed.
    """
    
    
    seen = set()
    unique_lists = []
    for sublist in list_of_lists:
        tuple_sublist = tuple(sublist)
        if tuple_sublist not in seen:
            seen.add(tuple_sublist)
            unique_lists.append(sublist)
    return unique_lists




def main():
    try:
        input_str = input("Enter the list of lists ")
        list_of_lists = eval(input_str)
        
        if not isinstance(list_of_lists, list) or any(not isinstance(i, list) for i in list_of_lists):
            raise ValueError("Input must be a list of lists.")
        
        new_list = remove_duplicates(list_of_lists)
        print("New List:", new_list)
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
