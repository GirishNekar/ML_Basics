'''
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title : Clear the set
'''

def clear_set(set1):
    
    
    """
    Description:
        Returns the union of two sets.
    Parameters:
        set1: The first set.
        set2: The second set.
    Returns:
        Cleared set
    """
    
    
    return set1.clear()

def main():

    set1 = {1, 2, 3, 4, 5, 6,9,10}
    print("set1:", set1)

    cleared_set = clear_set(set1)
    print(f'The set1 is cleared: {cleared_set}')


if __name__ == "__main__":
    main()
