'''

@Author: Girish
@Date: 2024-07-24 
@Last Modified by: Girish
@Last Modified time: 2024-07-24 
@Title : Listing Files in a Directory

'''

import os



def list_files(directory):
    
    
    """
    
    Description:
        Lists all files in a specified directory.
    Parameter:
        directory : Directory to list the files 
    Return:
        none

    """
    

    if not os.path.isdir(directory):
        print("The specified path is not a valid directory.")
        return
    
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        if files:
            print("Files in the directory:")
            for file in files:
                print(file)
        else:
            print("No files found in the directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
        
    directory = input("Enter the directory path: ").strip()
    
    list_files(directory)


if __name__ == "__main__":
    main()
