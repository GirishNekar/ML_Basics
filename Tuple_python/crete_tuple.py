'''
@Author: Girish
@Date: 2024-07-29
@Last Modified by: Girish
@Last Modified time: 2024-07-29
@Title : Create Tuple from List
'''


def create_tuple(mylist):
    
    
    """
    Description:
        Converts a list into a tuple.
        
    Parameters:
        mylist (list): List of elements to be converted into a tuple.
        
    Returns:
        tuple: A tuple containing the elements of the list.
        
    """
    
    
    created_tuple = tuple(mylist)
    return created_tuple



def main():
    try:
        length_tuple = int(input("Enter the length of tuple: "))
        if length_tuple <= 0:
            raise ValueError("The length of the tuple must be greater than zero.")
        mylist = []
        
        for index in range(length_tuple):
            mylist.append(int(input(f"Enter element {index + 1}: ")))

        print(create_tuple(mylist))
    except ValueError as e:
        print(f"Invalid input: {e}")



if __name__ == "__main__":
    main()
