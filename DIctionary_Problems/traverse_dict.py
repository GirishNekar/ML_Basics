
"""
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-07-30
@Title: Iterating Over Dictionaries
"""



def iterate_dict(my_dict):
    
    
    """
    Iterates over a dictionary and prints its keys, values, and key-value pairs
    
    Parameters:
        my_dict (dict): The dictionary to iterate over.
        
    Returns:
        None
    """
    
    
    try:
        print("Iterating over keys:")
        for key in my_dict:
            print(key)
        
        print("\nIterating over values:")
        for value in my_dict.values():
            print(value)
        
        print("\nIterating over key-value pairs:")
        for key, value in my_dict.items():
            print(f"Key: {key}, Value: {value}")
    
    except Exception as e:
        print(f"An error occurred: {e}")



def main():
    try:
        sample_dict = {}
        
        num_entries = int(input("Enter the number of dictionary entries: "))
        if num_entries <= 0:
            raise ValueError("The number of entries must be a positive integer.")
        
        for _ in range(num_entries):
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            sample_dict[key] = value
        
        iterate_dict(sample_dict)
    
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
