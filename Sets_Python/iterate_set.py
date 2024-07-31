'''

@Author: Girish
@Date: 2024-07-29 
@Last Modified by: Girish
@Last Modified time: 2024-07-29 
@Title : Iterate Over Set

'''



def iter_over_set(iter_set):
    
    
    """
    Description:
        Iterates over a set and prints each element.
        
    Parameters:
        iter_set (set): The set to be iterated over.
        
    Returns:
        None
    """
    
    
    for element in iter_set:
        print(element)



def main():
    try:
        iter_set = {1, "Girish", 0.02, True}
        iter_over_set(iter_set)
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
