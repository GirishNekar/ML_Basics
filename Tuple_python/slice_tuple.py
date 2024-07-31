'''
@Author: Girish
@Date: 2024-07-29
@Last Modified by: Girish
@Last Modified time: 2024-07-29
@Title : Slicing a Tuple
'''



def main():
    
    
    """
    Description:
        Creates a tuple and demonstrates slicing operations on it.
        
    Parameters:
        None
        
    Returns:
        None
    """
    
    
    my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

    print("Original tuple:", my_tuple)
    print("Elements from index 2 to 5:", my_tuple[2:6])
    print("Elements from the beginning to index 4:", my_tuple[:5])
    print("Elements from index 6 to the end:", my_tuple[6:])
    print("Last 3 elements:", my_tuple[-3:])
    print("Every 2nd element:", my_tuple[::2])



if __name__ == "__main__":
    main()
