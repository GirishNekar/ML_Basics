"""
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title: Print Unique Values in Dictionary
"""

def get_unique_values(dict_list):
    
    
    """
    Extracts and returns unique values from a list of dictionaries.
    
    Parameters:
        dict_list (list): A list of dictionaries from which to extract unique values.
        
    Returns:
        set: A set of unique values extracted from the dictionaries.
    """
    
    
    unique_values = set()
    try:
        for d in dict_list:
            for value in d.values():
                unique_values.add(value)
    except Exception as e:
        print(f"An error occurred: {e}")
    return unique_values



def main():
    try:
        # Sample data for demonstration
        sample_data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
                       {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
        
        print(f"Sample data: {sample_data}")
        
        unique_values = get_unique_values(sample_data)
        print(f"Unique Values: {unique_values}")
    
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
