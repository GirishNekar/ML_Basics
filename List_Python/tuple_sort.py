'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Sort List of Tuples by Last Element
'''



def sort_tuples_by_last_element(tuple_list):
    
    
    """
    Description:
        Sorts a list of non-empty tuples in increasing order by the last element in each tuple.
        
    Parameters:
        tuple_list (list): The list of non-empty tuples.
        
    Returns:
        list: The sorted list of tuples.
    """
    
    
    return sorted(tuple_list, key=lambda x: x[-1])



def main():
    
    
    try:
        tuple_list = []
        no_of_tuples = int(input("Enter the number of tuples: "))
        if no_of_tuples <= 0:
            raise ValueError("The number of tuples must be a positive integer.")

        for index in range(no_of_tuples):
            tuple_input = input(f"Enter tuple {index + 1} (comma-separated values): ")
            tuple_elements = tuple(map(int, tuple_input.split(',')))
            tuple_list.append(tuple_elements)

        sorted_list = sort_tuples_by_last_element(tuple_list)
        print(f"The sorted list of tuples is: {sorted_list}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    main()
