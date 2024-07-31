'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Difference Between Two Lists
'''


def list_difference(list1, list2):
    
    
    """
    Description:
        Computes the difference between two lists, returning items present in
        the first list but not in the second list.
        
    Parameters:
        list1 (list): The first list from which differences are computed.
        list2 (list): The second list to compare against.
        
    Returns:
        list: A list containing elements that are in list1 but not in list2.
    """
    
    
    result = []
    for item in list1:
        found = False
        for elem in list2:
            if item == elem:
                found = True
                break
        if not found:
            result.append(item)
    return result



def main():
    try:
        list1 = input("Enter the elements of the first list separated by commas: ").split(",")
        list2 = input("Enter the elements of the second list separated by commas: ").split(",")
        
        diff = list_difference(list1, list2)
        print("Difference between the two lists:", diff)
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
