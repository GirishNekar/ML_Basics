

'''

@Author: Girish
@Date: 2024-07-24 
@Last Modified by: Girish
@Last Modified time: 2024-07-24 
@Title : Finding day of a week for given date


'''


import builtins

def print_function_docs(func):
    
    
    """
    
    Description:
        prints documents of thee function  
    Parameter:
        func: function for which document needed to be printed
    Return:
        none
         

    """  
    
    
    try:
        # Check if the function is callable
        if not callable(func):
            raise ValueError("The provided input is not a callable function.")
        
        # Get the documentation string
        doc = func.__doc__
        if doc is None:
            raise ValueError("Documentation not found for the provided function.")
        
        # Print the documentation
        print(f"{func.__name__}()")
        print(doc)
        print("-" * 40)
    
    except ValueError as ve:
        print(f"Value Error: {ve}")


def list_builtin_functions():
    functions = [name for name in dir(builtins) if callable(getattr(builtins, name))]
    return functions

def main():
    # List all built-in functions
    functions = list_builtin_functions()
    
    print("Built-in functions:")
    for i, func_name in enumerate(functions):
        print(f"{i + 1}: {func_name}")
    

    choice = int(input("\nEnter the number of the function to get documentation (0 to exit): "))
        
    if choice == 0:
        print("Exiting...")
        return
        
    if 1 <= choice <= len(functions):
        func_name = functions[choice - 1]
        func = getattr(builtins, func_name)
        print_function_docs(func)
    else:
        print("Invalid choice. Please enter a number from the list.")


if __name__ == '__main__':
    main()
