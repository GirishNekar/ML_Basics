

'''

@Author: Girish
@Date: 2024-07-24 
@Last Modified by: Girish
@Last Modified time: 2024-07-24 
@Title : Finding Unique from 2 lists

'''

def Unique(color_set_2,color_list_1):


    """
    
    Description:
        prints list of Unique colours  
        
    Parameter:
        color_set_2 : set of colour_list_2
        colour_list_1 : colour_list1
        
    Return:
        none
         

    """


    unique_colors = [color for color in color_list_1 if color not in color_set_2]

    print("Colors in color_list_1 not in color_list_2:", unique_colors)


def main():
    
    
    color_list_1 = ["White", "Black", "Red"]
    color_list_2 = ["Red", "Green"]

    color_set_2 = set(color_list_2)
    
    Unique(color_set_2)
    


if __name__ == "__main__":
    main()