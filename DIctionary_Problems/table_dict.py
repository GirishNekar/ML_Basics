"""
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title: Print Dictionary in Table Format
"""


def print_dict_in_table_format(data_dict):
    
    
    """
    Prints a dictionary in a table format.
    
    Parameters:
        data_dict (dict): The dictionary to be printed.
        
    Returns : none
    
    """
    
    
    try:
        longest_key = max(len(str(key)) for key in data_dict.keys())
        longest_value = max(len(str(value)) for value in data_dict.values())


        print(f"{'Key'.ljust(longest_key)} | {'Value'.ljust(longest_value)}")
        print("-" * (longest_key + longest_value + 3))

       
        for key, value in data_dict.items():
            print(f"{str(key).ljust(longest_key)} | {str(value).ljust(longest_value)}")

    except Exception as e:
        print(f"An error occurred: {e}")



def main():
    try:
        sample_dict = {
            'name': 'Alice',
            'age': 30,
            'city': 'New York',
            'email': 'alice@example.com'
        }

        print("Dictionary in Table Format:")
        print_dict_in_table_format(sample_dict)
    
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
