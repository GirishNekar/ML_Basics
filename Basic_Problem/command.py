'''

@Author: Girish
@Date: 2024-07-24 
@Last Modified by: Girish
@Last Modified time: 2024-07-24 
@Title : Executing User-Input Commands in Python

'''

import subprocess
import platform

def execute_command(command):
    
    
    """
    
    Description:
        Executes a user-input command using subprocess module and prints the output.
    Parameter:
        command : command to execute
    Return:
        none

    """

    
    try:
        result = subprocess.run(command, shell=True,capture_output=True, text=True, check=True)
        print("Command Output:\n", result.stdout)
        if result.stderr:
            print("Errors:\n", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e}")
    except FileNotFoundError:
        print("Error: Command not found. Please ensure the command is correct and available on your system.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def main():
    
    command = input("Enter the command you want to execute (e.g., Dir): ").strip().split()
    execute_command(command)


if __name__ == "__main__":
    main()
