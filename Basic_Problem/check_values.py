'''

@Author: Girish
@Date: 2024-07-24 
@Last Modified by: Girish
@Last Modified time: 2024-07-24 
@Title : Finding day of a week for given date


'''


def check_in_mylist(mylist):
    
    
    """
    
    Description:
        Returns true if the Entered number present in the mylist 
    Parameter:
        mylist : list of intergers cretated
    Return:
        returns true if the number is pressent
         

    """   
    
    
    try:
        
        inpt = int(input("Enter the Number to search in the mylist"))
        
        if(inpt.isdigit() == False):
            raise ValueError(f'Pleasse Enter only the numbers')
        
    except ValueError as e:
        print(f'{e}') 
        
        if inpt in mylist:
            return True
        else:
            return False

def main():
  
    mylist = []
    for i in range(100):
        mylist.append(i)
    x = mylist
    print(check_in_mylist(x))



if __name__ == "__main__":
    main()