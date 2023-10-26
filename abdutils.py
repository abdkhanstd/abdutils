# This is my Python utility file that I've created to address certain issues and simplify my own programming.
# Version 001
# Visit https://github.com/abdkhanstd/abdutils

import os
import shutil
import warnings

def CreateFolder(path, mode="a", verbose=True):
    """
    Create a folder with the given path using one of the following modes:

    - 'f' (force_create): Deletes the folder if it already exists and then creates it.
    - 'o' (overwrite): Overwrites the folder if it already exists.
    - 'c' (create_if_not_exist): Creates the folder if it doesn't exist.
    - 'a' (ask_user): Asks the user whether to delete and overwrite, or just pass if the folder exists.

    Args:
        path (str): The path to the folder to be created.
        mode (str): The mode for folder creation ('f', 'o', 'c', or 'a'). Defaults to 'a' (ask_user).
        verbose (bool): Whether to display verbose messages. Defaults to True.
        
    Examples:    
        # Example 1: Create a folder using the default "ask_user" mode with verbose messages
        CreateFolder(path, verbose=True)  # Ask user (recursively)
        
        # Example 2: Create a folder recursively with a long path without verbose messages
        long_path = "parent/child/grandchild"
        CreateFolder(long_path, verbose=False)  # Create if not exist (recursively)
        
        # Example 3: Force create a folder, displaying a message
        CreateFolder("folder_to_force_create", mode="f", verbose=True)
        
        # Example 4: Overwrite a folder, displaying a message
        CreateFolder("folder_to_overwrite", mode="o", verbose=True)
        
        # Example 5: Create a folder if it doesn't exist, displaying a message
        CreateFolder("folder_to_create_if_not_exist", mode="c", verbose=True)
        
        # Example 6: Ask the user whether to delete and recreate a folder, displaying a message
    CreateFolder("folder_to_ask_user", mode="a", verbose=True)        
    """
    try:
        if mode == "f":  # force_create
            if os.path.exists(path):
                if verbose:
                    print(f"Info: The folder '{path}' already exists. Deleting and recreating.")
                    shutil.rmtree(path)
            os.makedirs(path, exist_ok=True)  # Create folder recursively
        elif mode == "o":  # overwrite
            if os.path.exists(path):
                if verbose:
                    print(f"Info: The folder '{path}' already exists. Overwriting.")
                    shutil.rmtree(path)
            os.makedirs(path, exist_ok=True)  # Create folder recursively
        elif mode == "c":  # create_if_not_exist
            if os.path.exists(path):
                if verbose:
                    print(f"Info: The folder '{path}' already exists. Skipping creation.")
            else:
                os.makedirs(path, exist_ok=True)  # Create folder recursively
        elif mode == "a":  # ask_user
            if os.path.exists(path):
                user_input = input(f"The folder '{path}' already exists. Do you want to delete and overwrite it? (y/n): ")
                if user_input.lower() == "y":
                    if verbose:
                        print(f"Info: The folder '{path}' already exists. Deleting and recreating.")
                        shutil.rmtree(path)
                    os.makedirs(path, exist_ok=True)  # Create folder recursively
                else:
                    print("Folder creation aborted.")
        else:
            raise ValueError(f"Invalid mode '{mode}'. Please use 'f' (force_create), 'o' (overwrite), 'c' (create_if_not_exist), or 'a' (ask_user).")
    except Exception as e:
        print(f"An error occurred while creating the folder: {str(e)}")


def ReadFile(file_path):
    """
    Read a file line by line and return one line at a time with each function call.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The next line from the file.
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        yield None

    
    
def WriteFile(file_path, lines, mode="w"):
    """
    Write lines to a file in either append or write mode.

    Args:
        file_path (str): The path to the file to be written.
        lines (str or list of str): The lines to be written to the file.
        mode (str): The mode for writing the file ('w' for write, 'a' for append). Defaults to 'w'.
    """
    try:
        with open(file_path, mode) as file:
            if isinstance(lines, str):
                # If 'lines' is a string, write it as a single line
                file.write(lines + '\n')
            elif isinstance(lines, list):
                # If 'lines' is a list of strings, write each string as a separate line
                for line in lines:
                    file.write(line + '\n')
    except Exception as e:
        print(f"An error occurred while writing to the file: {str(e)}")
