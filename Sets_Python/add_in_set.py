'''

@Author: Girish
@Date: 2024-07-29 
@Last Modified by: Girish
@Last Modified time: 2024-07-29 
@Title : Add Elements to Set

'''

def add_element(my_set):
    
    
    """
    Description:
        Adds elements to the provided set based on user input.
        
    Parameters:
        my_set (set): The set to which elements will be added.
        
    Returns:
        set: The updated set with added elements.
    """
    
    
    for index in range(10):
        my_set.add(int(input("Enter the element to add to the set: ")))
    return my_set




def main():
    
    try:
        my_set = set()
        added_set = add_element(my_set)
        print("Updated set:", added_set)
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
