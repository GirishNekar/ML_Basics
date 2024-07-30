'''

@Author: Girish
@Date: 2024-07-24 
@Last Modified by: Girish
@Last Modified time: 2024-07-24 
@Title : Checking if a file exists

'''

import os



def check_file_path(file_path):
    
    
    """
    
    Description:
        Checks whether a specified file exists and prints the result.
    Parameter:
        none
    Return:
        none
         

    """
    
    
    
    if os.path.isfile(file_path):
        print(f"The file '{file_path}' exists.")
    else:
        print(f"The file '{file_path}' does not exist.")
    

def main():
    
    
    file_path = input("Enter the file path to check: ")
    check_file_path(file_path)


if __name__ == "__main__":
    main()
