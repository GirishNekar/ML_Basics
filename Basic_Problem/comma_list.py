



'''

@Author: Girish
@Date: 2024-07-24 
@Last Modified by: Girish
@Last Modified time: 2024-07-24 
@Title : Finding day of a week for given date


'''

def split_comma(mylist,newlist):

    """
    
    Description:
        prints list and tuple of comma seperated integer  
        
    Parameter:
        mylist: list of comma seperated integers
        
    Return:
        none
         

    """

    try: 
        for i in mylist:
            if i != "":
                newlist.append(i)
                
        for item in newlist:
            if not item.strip().isdigit():
                raise ValueError(f"Invalid input: '{item}' is not a number.")

        # Convert the list to a tuple
        tup = tuple(newlist)
        
        print("List:", newlist)
        print("Tuple:", tup)
        
    except ValueError as ve:
        print(f"Value Error: {ve}")



def main():    
        
    user_input = input("Enter the numbers separated with commas: ")
    mylist = user_input.split(',')
    newlist = []
              
    split_comma(mylist,newlist)



if __name__ == '__main__':
    main()