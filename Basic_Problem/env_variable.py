'''

@Author: Girish
@Date: 2024-07-24 
@Last Modified by: Girish
@Last Modified time: 2024-07-24 
@Title : Accessing Environment Variables in Python

'''

import os

def main():
    
    """
    
    Description:
        Accesses and prints specific environment variables and all environment variables.
        
    Parameter:
        none
        
    Return:
        none

    """

    # Access a specific environment variable
    specific_var = "PATH"  # Example environment variable
    path_value = os.getenv(specific_var)
    
    if path_value:
        print(f"{specific_var} environment variable: {path_value}")
    else:
        print(f"{specific_var} environment variable is not set.")
    
    # Access and print all environment variables
    print("\nAll Environment Variables:")
    for key, value in os.environ.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
