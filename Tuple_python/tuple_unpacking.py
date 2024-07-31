'''
@Author: Girish
@Date: 2024-07-11
@Last Modified by: Girish
@Last Modified time: 2024-07-11
@Title : Unpack a Tuple into Several Variables
'''

def unpack_tuple(my_tuple):
    
    
    """
    Description:
        Unpacks a given tuple into several variables.
        
    Parameters:
        my_tuple (tuple): The tuple to be unpacked.
        
    Returns:
        tuple: A tuple of unpacked variables.
    """
    
    
    Name, Place, roll_no = my_tuple
    return Name, Place, roll_no

def main():
    try:
        my_tuple = ("Girish", "Bangalore", 50)
        Name, Place, roll_no = unpack_tuple(my_tuple)
        print(f'Name: {Name}')
        print(f'Place: {Place}')
        print(f'Roll no: {roll_no}')
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
