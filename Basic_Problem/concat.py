

'''

@Author: Girish
@Date: 2024-07-24 
@Last Modified by: Girish
@Last Modified time: 2024-07-24 
@Title : Finding day of a week for given date


'''

def is_alpha(string):
    
    """
    
    Description:
        Checks if string contains only alpabetic charecters  
    Parameter:
        string : String needed to be checked
    Return:
        True if string contains only alpabetic charecters else False
         

    """  
    
    return string.isalpha()

def concatenate_list(lst):
    
    """
    
    Description:
        Checks if string contains only alpabetic charecters  
    Parameter:
        string : String needed to be checked
    Return:
        True if string contains only alpabetic charecters else False
         

    """
    
    
    
    return ' '.join(lst)

def main():
    lst = []
    
    while True:
        try:
            user_input = input("Enter a string (alphabetic characters only) or 'STOP' to finish: ")
            
            if user_input.upper() == 'STOP':
                break 
            
            if not is_alpha(user_input):
                raise ValueError("Please enter alphabetic characters only.")
            
            lst.append(user_input)
        
        except ValueError as e:
            print(f"Error: {e}")
    
    concatenated_string = concatenate_list(lst)
    print("Concatenated String:", concatenated_string)

if __name__ == "__main__":
    main()
