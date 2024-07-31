'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Remove Specific Elements from List
'''



def remove_elements(mylist):
    
    
    """
    Description:
        Removes the 0th, 4th, and 5th elements from the provided list.
        
    Parameters:
        mylist (list): The list from which elements will be removed.
        
    Returns:
        list: The modified list after removal of specified elements.
    """
    
    
    if len(mylist) < 6:
        return mylist
    mylist.pop(5)
    mylist.pop(4)
    mylist.pop(0)
    return mylist

def main():
    try:
        input_list = input("Enter the list of elements separated by commas: ").split(",")
        modified_list = remove_elements(input_list)
        print("Modified list:", modified_list)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
