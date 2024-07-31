'''
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title : Traverse a Frozen Set
'''


def traverse(frozen_set):
    
    
    """
    Description:
        Traverses the elements in a frozen set and prints them.
    Parameters:
        frozen_set: The frozen set to be traversed.
    Returns:
        None
    """
    
    
    for element in frozen_set:
        print(element)
        
        
        

def main():
    
    set1 = {1, 2, 3, 4, 5, "Girish", 20.5}
    frozen_set = frozenset(set1)
    print(f"Frozen set: {frozen_set}")
    traverse(frozen_set)



if __name__ == "__main__":
    main()
