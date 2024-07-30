"""
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title: Generate Dictionary with Numbers and Their Squares
"""


def generate_dict(n):
    
    
    """
    Generates a dictionary with numbers between 1 and n in the form (x, x*x).
    
    Parameters:
        n (int): The upper limit for the dictionary keys.
        
    Returns:
        dict: A dictionary with numbers as keys and their squares as values.
    """
    
    result_dict = {x: x*x for x in range(1, n+1)}
    return result_dict
 
 

def main():
    try:
        n = int(input("Enter the upper limit (n) for generating the dictionary: "))
        if n <= 0:
            raise ValueError("The number must be a positive integer.")
        
        generated_dict = generate_dict(n)
        print(f"Generated dictionary: {generated_dict}")
    
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
