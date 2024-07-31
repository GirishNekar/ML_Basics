'''
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title : Union of Two Sets
'''

def union_of_sets(set1, set2):
    
    
    """
    Description:
        Returns the union of two sets.
    Parameters:
        set1: The first set.
        set2: The second set.
    Returns:
        A set that contains the union of set1 and set2.
    """
    
    
    return set1.union(set2)

def main():

    set1 = {1, 2, 3, 4, 5, 6}
    print("Set 1:", set1)

    set2 = {7, 8, 9, 10, 11}
    print("Set 2:", set2)

    union_set = union_of_sets(set1, set2)
    print(f'Union of set1 and set2 is: {union_set}')


if __name__ == "__main__":
    main()
