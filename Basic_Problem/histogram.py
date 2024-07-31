

'''

@Author: Girish
@Date: 2024-07-25 
@Last Modified by: Girish
@Last Modified time: 2024-07-24 
@Title : printing histogram of list of integers

'''


def create_histogram(numbers):
    
    """
    
    Description:
        Creates the histogram for list og intergers 
        
    Parameter:
        numbers : list of numbers used to prepare histogram 
        
    Return:
        None
         

    """    
    
    
    # Initialize an empty dictionary to count the frequency of each number
    frequency = {}

    # Count the frequency of each number in the list 
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    
    # Print the histogram
    print("Histogram:")
    for number, count in frequency.items():
        print(f"{number}: {'*' * count}")

# Example list of integers

def main():
    try:
        mylist = []
        length = int(input("Enter the length of the array: "))
        
        if length <= 0:
            raise ValueError("Length must be greater than 0")

        for i in range(length):
            try:
                x = int(input(f"Enter number {i+1}: "))
                mylist.append(x)
            except ValueError:
                print("Invalid input. Please enter an integer.")
                return  # Exit the program on invalid input
        
        print("Input list:", mylist)
        create_histogram(mylist)

    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()
