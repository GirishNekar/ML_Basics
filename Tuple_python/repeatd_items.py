'''
@Author: Girish
@Date: 2024-07-29
@Last Modified by: Girish
@Last Modified time: 2024-07-29
@Title : Remove Duplicates from Tuple and Find Repeated Elements
'''

def remove_duplicates(input_list):
    
    
    """
    Description:
        Removes duplicates from the provided list.
    Parameter:
        input_list (list): The list from which duplicates are to be removed.
    Return:
        list: A list with duplicates removed.
    """
    
    
    unique_list = []
    for number in input_list:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list

def find_repeated_elements(input_list):
    
    
    
    """
    Description:
        Finds and returns the repeated elements from the provided list.
    Parameter:
        input_list (list): The list from which repeated elements are to be identified.
    Return:
        list: A list containing repeated elements.
    """
    
    
    
    repeated_list = []
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] == input_list[j] and input_list[i] not in repeated_list:
                repeated_list.append(input_list[i])
    return repeated_list




def main():
    try:
        user_input = input("Enter a tuple of numbers separated by commas :")
        user_input_list = user_input.split(',')
        
        list_1 = [int(x) for x in user_input_list]
        
        unique_list = remove_duplicates(list_1)
        unique_tuple = tuple(unique_list)
        
        repeated_list = find_repeated_elements(list_1)
        repeated_tuple = tuple(repeated_list)
        
        print("Original tuple:", tuple(list_1))
        print("Unique elements:", unique_tuple)
        print("Repeated elements:", repeated_tuple)
        
    except ValueError:
        print("Please enter valid integers separated by commas.")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
