
'''
@Author: Girish
@Date: 2024-07-26
@Last Modified by: Girish
@Last Modified time: 2024-07-26
@Title : Sort Alphanumeric List with Exception Handling
'''

def sort_alpha_numeric(sentence_list):
    
    
    """
    Description:
        Sorts a list of alphanumeric strings in ascending order.
        
    Parameters:
        sentence_list (list): The list of strings to sort.
        
    Returns:
        list: A new list containing the sorted strings.
    """
    
    
    return sorted(sentence_list)

def main():

    try:
        sentence = input("Enter the sentence separated by commas only: ").strip()
        if not sentence:
            raise ValueError("The input cannot be empty.")
        
        sentence_list = [s.strip() for s in sentence.split(",")]
        if not all(sentence_list):
            raise ValueError("Ensure all list items are non-empty strings.")
        
        sorted_list = sort_alpha_numeric(sentence_list)
        print("Sorted list:", sorted_list)
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()


