'''

@Author: Girish
@Date: 2024-07-24 
@Last Modified by: Girish
@Last Modified time: 2024-07-24 
@Title : Finding Number of CPUs in Python

'''

import os


def count_cpu():
    
   
    """
    
    Description:
        Finds and prints the number of CPUs available on the system using the os module.
        
    Parameter:
        none
        
    Return:
        none

    """ 
    
    
    num_cpus = os.cpu_count()
    
    if num_cpus is not None:
        print(f"Number of CPUs available: {num_cpus}")
    else:
        print("Unable to determine the number of CPUs.")



def main():
    
    count_cpu()


if __name__ == "__main__":
    main()
