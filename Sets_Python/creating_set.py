'''

@Author: Girish
@Date: 2024-07-29 
@Last Modified by: Girish
@Last Modified time: 2024-07-29 
@Title : Create Non-Empty and Empty Sets

'''


def create_non_empty_set():
    
    
    """
    Description:
        Creates and returns a non-empty set.
        
    Returns:
        set: A non-empty set with different types of elements.
    """
    
    
    return {"Girish", 1, 2, 0.03}



def create_empty_set():
    
    
    """
    Description:
        Creates and returns an empty set.
        
    Returns:
        set: An empty set.
    """
    
    
    return set()



def main():
    try:
        empty_set = create_empty_set()
        print("Empty set is:", empty_set)
        
        non_empty_set = create_non_empty_set()
        print("Non Empty set is:", non_empty_set)
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
