'''
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title : Find Max and Min in a Set
'''


def max_min(myset):
    
    
    """
    
    Description:
        Finds the maximum and minimum elements in the provided set.
        
    Parameters:
        myset (set): The set from which to find the max and min.
        
    Returns:
        list: A list containing the maximum and minimum elements.
        
    """
    
    
    max_in_set = max(myset)
    min_in_set = min(myset)
    return [max_in_set, min_in_set]




def main():
       
    try:
        myset = set()
        n = int(input("Enter the number of elements to add to the set: "))
        
        for index in range(n):
            x = int(input("Enter a number to add to the set: "))
            myset.add(x)

        result = max_min(myset)
        print(f"The maximum element in the set is: {result[0]}")
        print(f"The minimum element in the set is: {result[1]}")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
