

'''
@Author: Girish
@Date: 2024-07-29
@Last Modified by: Girish
@Last Modified time: 2024-07-29
@Title : Slicing a Tuple
'''


def reverse_tuple(tup):
    
    
        
    """
    Description:
        Reverses the given tuple.
    
    Parameters:
        tup (tuple): The tuple to be reversed.
    
    Returns:
        tuple: A new tuple that is the reversed version of the input tuple.
    """
    
    
    
    reversed_tup = ()
    for i in range(len(tup) - 1, -1, -1):
        reversed_tup += (tup[i],)
    return reversed_tup


def main():

    try:
        num_elements = int(input("Enter the number of elements in the tuple: "))
        my_tuple = tuple(input(f"Enter element {i + 1}: ") for i in range(num_elements))
        
        print(f'Original tuple: {my_tuple}')
        
        reversed_tuple = reverse_tuple(my_tuple)
        print(f'Reversed tuple: {reversed_tuple}')
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
