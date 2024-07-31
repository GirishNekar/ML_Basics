'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Words Longer Than N
'''

def words_longer_than_n(words_list, n):
    
    
    """
    Description:
        Filters words from the given list that are longer than the specified length n.
        
    Parameters:
        words_list (list): The list of words to filter.
        n (int): The length to compare against.
        
    Returns:
        list: A list of words longer than length n.
    """
    
    
    return [word for word in words_list if len(word) > n]




def main():
    try:
        length = int(input("Enter the number of words in the list: "))
        if length <= 0:
            raise ValueError("The number of words must be a positive integer.")
        words_list = []
        for index in range(length):
            word = input(f"Enter word {index + 1}: ")
            words_list.append(word)
        n = int(input("Enter the length to compare against: "))
        result = words_longer_than_n(words_list, n)
        print(f"Words longer than {n}: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
