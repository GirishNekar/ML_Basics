'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Check Common Member in Lists
'''

def have_common_member(list1, list2):
    
    
    """
    Description:
        Checks if there is at least one common member between two lists.
        
    Parameters:
        list1 (list): The first list.
        list2 (list): The second list.
        
    Returns:
        bool: True if there is at least one common member, False otherwise.
    """
    
    
    for item in list1:
        if item in list2:
            return True
    return False



def main():
    try:
        list1 = input("Enter the first list of elements separated by commas: ").split(",")
        list2 = input("Enter the second list of elements separated by commas: ").split(",")
        result = have_common_member(list1, list2)
        print(f"Do the lists have at least one common member? {result}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
