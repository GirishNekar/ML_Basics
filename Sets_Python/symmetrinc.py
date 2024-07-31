'''
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title : Create Symmetric Difference of Two Sets
'''



def symmetric_difference(set1, set2):
    
    
    
    """
    Description:
        Calculates the symmetric difference between two sets.
    Parameters:
        set1 (set): The first set.
        set2 (set): The second set.
    Returns:
        set: A set containing the symmetric difference of set1 and set2.
    """
    
    
    result = (set1 - set2) | (set2 - set1)
    return result

def main():
  
    try:
        set1 = set()
        set2 = set()
        
        n1 = int(input("Enter the number of elements for the first set: "))
        for index in range(n1):
            x = int(input("Enter a number to add to the first set: "))
            set1.add(x)
        
        n2 = int(input("Enter the number of elements for the second set: "))
        for index in range(n2):
            y = int(input("Enter a number to add to the second set: "))
            set2.add(y)
        
        result = symmetric_difference(set1, set2)
        print(f"The symmetric difference of the two sets is: {result}")
    
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
