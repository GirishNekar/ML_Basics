'''

@Author: Girish
@Date: 2024-07-24 
@Last Modified by: Girish
@Last Modified time: 2024-07-24 
@Title : Finding day of a week for given date

'''


def reverse_name(first_name,last_name):
    
    
    """
    
    Description:
        prints the first name and last name in reverse order
    
    Parameter:
        first_name : first_name of the user
        last_name : last_name of the user
        
    Return:
        none

    """
    
    print(last_name+" "+first_name)


def main():
    
    
    try:
        first_name = str(input("Enter the First name "))
        last_name = str(input("enter the lat Name "))
        
        if not first_name.isalpha() or not last_name.isalpha():
            raise ValueError("Names Should contain only alphabetic cahrecters")
        
        reverse_name(first_name,last_name)
    except ValueError as ve:
        print(f'error : {ve}')
        


if __name__ == '__main__':
    main()