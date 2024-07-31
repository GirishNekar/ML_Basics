'''
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title : Intersection of Two Sets
'''



def intersection_of_sets(set1, set2):
    
    
    """
    Description:
        Returns the intersection of two sets.
    Parameters:
        set1: The first set.
        set2: The second set.
    Returns:
        A set that contains the intersection of set1 and set2.
    """
    
    
    return set1.intersection(set2)



def main():
    try:
        set1 = set()
        set2 = set()

        for _ in range(4):
            x = int(input("Enter the element for set1: "))
            set1.add(x)

        for _ in range(4):
            y = int(input("Enter the element for set2: "))
            set2.add(y)

        intersection_set = intersection_of_sets(set1, set2)
        print("Intersection of set1 and set2:", intersection_set)
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
