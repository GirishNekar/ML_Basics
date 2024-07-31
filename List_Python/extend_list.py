'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Append a List to Another List Without Inbuilt Functions
'''


def append_list(base_list, list_to_append):
    """
    Description:
        Appends the elements of one list to another without using built-in functions.
        
    Parameters:
        base_list (list): The list to which elements will be appended.
        list_to_append (list): The list whose elements will be appended to base_list.
        
    Returns:
        None
    """
    
    
    for item in list_to_append:
        base_list.append(item)



def main():
    try:
        base_list_input = input("Enter the elements of the base list separated by commas: ").split(",")
        list_to_append_input = input("Enter the elements of the list to append separated by commas: ").split(",")
        
        base_list = [elem.strip() for elem in base_list_input]
        list_to_append = [elem.strip() for elem in list_to_append_input]
        
        append_list(base_list, list_to_append)
        
        print("Base list after appending:", base_list)
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
