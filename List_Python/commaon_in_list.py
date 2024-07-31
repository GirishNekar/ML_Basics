'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Find Common Items From Two Lists
'''

def find_common_items(list1, list2):
    
    
    """
    Description:
        Finds common items between two lists.
        
    Parameters:
        list1 (list): The first list to compare.
        list2 (list): The second list to compare.
        
    Returns:
        list: A list containing common items between list1 and list2.
        
    """
    
    
    common_items = []
    for item in list1:
        if item in list2 and item not in common_items:
            common_items.append(item)
    return common_items



def main():
    try:
        list1_input = input("Enter the elements of the first list separated by commas: ").split(",")
        list2_input = input("Enter the elements of the second list separated by commas: ").split(",")
        
        list1 = [elem.strip() for elem in list1_input]
        list2 = [elem.strip() for elem in list2_input]
        
        common_items = find_common_items(list1, list2)
        print("Common items:", common_items)
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
