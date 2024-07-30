'''
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-27
@Title : Split List Based on First Character of Word
'''


def split_by_first_char(word_list):
    
    
    """
    Description:
        Splits a list of words into sublists based on the first character of each word.
        
    Parameters:
        word_list (list): The list of words to split.
        
    Returns:
        dict: A dictionary where keys are the first characters and values are lists of words that start with those characters.
    """
    
    
    split_dict = {}
    for word in word_list:
        first_char = word[0].lower()
        if first_char not in split_dict:
            split_dict[first_char] = []
        split_dict[first_char].append(word)
    return split_dict



def main():
    try:
        words_input = input("Enter words separated by commas: ").split(",")
        words_list = [word.strip() for word in words_input]
        
        split_result = split_by_first_char(words_list)
        for key, value in split_result.items():
            print(f"Words starting with '{key}': {value}")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
