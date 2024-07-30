'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Count Strings with Same First and Last Character
'''



def count_special_strings(string_list):
    
    
    """
    Description:
        Counts the number of strings where the string length is 2 or more and the first and last characters are the same.
        
    Parameters:
        string_list (list): The list of strings.
        
    Returns:
        int: The count of strings meeting the criteria.
    """
    
    
    count = 0
    for string in string_list:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count



def main():
    
    
    try:
        string_list = []
        no_of_strings = int(input("Enter the number of strings: "))
        if no_of_strings <= 0:
            raise ValueError("The number of strings must be a positive integer.")

        for index in range(no_of_strings):
            string = input(f"Enter string {index + 1}: ")
            string_list.append(string)

        special_string_count = count_special_strings(string_list)
        print(f"The number of special strings is: {special_string_count}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    main()
