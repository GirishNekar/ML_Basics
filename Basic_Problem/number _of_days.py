'''

@Author: Girish
@Date: 2024-07-25 
@Last Modified by: Girish
@Last Modified time: 2024-07-25 
@Title : Finding day of a week for given date

'''

def days_bwn_two(y1,m1,d1,y2,m2,d2):
    
    """
    
    Description:
        Calulates the nimber of sdays between Two given Dates 
    Parameter:
        year1,month1,date1,year2,month2,date2 - year month and dates of two different days 
    Return:
        prints number of days
         

    """
    
    no_of_days = (d2-d1) + (m2-m1)*30 + (y2 - y1) * 365
    print(f"number of days between two provided dates{no_of_days}")
    

def main():

    
    try:
        print("Enter the First Date")
        year1 = int(input("Enter the 1st Year"))
        month1 = int(input("Enter the 1st month "))
        date1 = int(input("Enter the 1st date date"))
        
  
        print("Enter the Second Date")
        year2 = int(input("Enter the 2nd Year"))
        month2 = int(input("Enter the 2nd month "))
        date2 = int(input("Eter the 2nd date date"))
        
        
        if type(year2) != int or type(month2) != int or type(date2) != int or type(year1) != int or type(month1) != int or type(date1) != int:
            raise ValueError("Please Enter the Valid Values")    
    except ValueError as e:
        print(f"{e}")
        
        
    days_bwn_two(year1,month1,date1,year2,month2,date2)
        

if __name__ == '__main__':
    main()