'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Check Whether Two Lists Are Circularly Identical
'''

def are_circularly_identical(list1, list2):
    
    
    """
    
    Description:
        Checks whether two lists are circularly identical.
        
    Parameters:
        list1 (list): The first list to compare.
        list2 (list): The second list to compare.
        
    Returns:
        bool: True if the lists are circularly identical, False otherwise.
        
    """
    
    
    if len(list1) != len(list2):
        return False
    
    combined_list = list1 + list1
    for i in range(len(list1)):
        if combined_list[i:i + len(list2)] == list2:
            return True
    return False



def main():
    try:
        list1_input = input("Enter the elements of the first list separated by commas: ").split(",")
        list2_input = input("Enter the elements of the second list separated by commas: ").split(",")
        
        list1 = [elem for elem in list1_input]
        list2 = [elem for elem in list2_input]
        
        result = are_circularly_identical(list1, list2)
        if result:
            print("The lists are circularly identical.")
        else:
            print("The lists are not circularly identical.")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
