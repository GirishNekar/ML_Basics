

'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Generate All Permutations of a List
'''


def permute(arr, start, end, result):
    
    
    """
    Description:
    
        Recursively generates all permutations of the list by swapping elements.
        
    Parameters:
    
        arr (list): The list of elements to permute.
        start (int): The starting index for permutations.
        end (int): The ending index for permutations.
        result (list): A list to collect all permutations.
        
    Returns:
    
        None
    """
    
    
    if start == end:
        result.append(arr.copy())
    else:
        for i in range(start, end + 1):
            arr[start], arr[i] = arr[i], arr[start]
            permute(arr, start + 1, end, result)
            arr[start], arr[i] = arr[i], arr[start]



def generate_permutations(input_list):
    
    
    """
    Description:
        Initializes the recursive permutation generation.
        
    Parameters:
        input_list (list): The list for which permutations will be generated.
        
    Returns:
        list: A list of lists, each containing a permutation of the input_list.
    """
    
    
    result = []
    permute(input_list, 0, len(input_list) - 1, result)
    return result

    

def main():
    try:
        input_list = input("Enter the list of elements separated by commas: ").split(",")
        perms = generate_permutations(input_list)
        print("All permutations:")
        for perm in perms:
            print(perm)
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
