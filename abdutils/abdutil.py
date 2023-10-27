__version__ = '0.1'
import os
import shutil
import warnings
import cv2
import numpy as np
from PIL import ImageFilter  # Import ImageFilter from PIL (Pillow)
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
import inspect
import sys
from PIL import Image

import os
import glob

def ReadDirectoryContents(path_pattern, verbose=True):
    """
    Reads the contents of a directory based on the provided pattern and returns a list of matched items.

    Args:
        path_pattern (str): The path pattern to match files and directories. 
                            For example: '/home/tt/*.jpg' or '/home/tt/*.*' or '/home/tt/'
        verbose (bool): Whether to display verbose messages. Defaults to True.

    Returns:
        list: A list of matched items based on the provided pattern.
    """
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename
    
    try:
        matched_items = glob.glob(path_pattern)
        if verbose:
            print(f"Found {len(matched_items)} items matching the pattern '{path_pattern}'.")

        return matched_items

    except Exception as e:
        HandleError(str(e), caller_filename, caller_line)
        return []


def CopyFile(src_pattern, dest_folder, verbose=True):
    """
    Copies files from the source pattern to the destination folder.

    Args:
        src_pattern (str): The source file pattern. Supports regular expressions like '/path/to/files/*.txt'.
        dest_folder (str): The destination folder where files will be copied.
        verbose (bool): Whether to display verbose messages. Defaults to True.
    """
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename
    
    try:
        matched_files = glob.glob(src_pattern)
        
        if not matched_files:
            if verbose:
                print(f"No files found matching the pattern '{src_pattern}'.")
            return

        CreateFolder(dest_folder, mode="f", verbose=verbose)

        for file_path in matched_files:
            shutil.copy(file_path, dest_folder)
            if verbose:
                print(f"Copied '{file_path}' to '{dest_folder}'.")

    except Exception as e:
        HandleError(str(e), caller_filename, caller_line)


def MoveFolder(original_path, new_path, verbose=True):
    """Move a folder from the original path to the new path."""
    caller_frame = sys._getframe(1)
    caller_line = caller_frame.f_lineno
    caller_filename = caller_frame.f_globals.get('__file__')
    try:
        folder = os.path.dirname(new_path)
        CreateFolder(folder, mode="f")

        shutil.move(original_path, new_path)
        if verbose:
            print(f"Folder '{original_path}' moved to '{new_path}'.")

    except Exception as e:
        HandleError(str(e), caller_filename, caller_line)

def MoveFile(src_pattern, dest_folder, verbose=True):
    """
    Moves files from the source pattern to the destination folder.

    Args:
        src_pattern (str): The source file pattern. Supports regular expressions like '/path/to/files/*.txt'.
        dest_folder (str): The destination folder where files will be moved.
        verbose (bool): Whether to display verbose messages. Defaults to True.
    """
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename
    
    try:
        matched_files = glob.glob(src_pattern)
        
        if not matched_files:
            if verbose:
                print(f"No files found matching the pattern '{src_pattern}'.")
            return

        CreateFolder(dest_folder, mode="f", verbose=verbose)

        for file_path in matched_files:
            shutil.move(file_path, dest_folder)
            if verbose:
                print(f"Moved '{file_path}' to '{dest_folder}'.")

    except Exception as e:
        HandleError(str(e), caller_filename, caller_line)

def RenameFileFolder(src_pattern, dest_name, verbose=True):
    """
    Renames a file or folder based on the provided source pattern.

    Args:
        src_pattern (str): The source file/folder pattern. Supports regular expressions like '/path/to/files/fileprefix*'.
        dest_name (str): The new name for the file/folder.
        verbose (bool): Whether to display verbose messages. Defaults to True.
    """
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename
    
    try:
        matched_files_folders = glob.glob(src_pattern)
        
        if not matched_files_folders:
            if verbose:
                print(f"No files or folders found matching the pattern '{src_pattern}'.")
            return
        
        if len(matched_files_folders) > 1:
            msg = f"Multiple files or folders matched the pattern '{src_pattern}'. Please be more specific."
            HandleError(msg, caller_filename, caller_line)
            return

        src_path = matched_files_folders[0]
        dest_path = os.path.join(os.path.dirname(src_path), dest_name)
        
        os.rename(src_path, dest_path)
        
        if verbose:
            print(f"Renamed '{src_path}' to '{dest_path}'.")

    except Exception as e:
        HandleError(str(e), caller_filename, caller_line)

import os
import shutil

def DeleteFileFolder(path, verbose=True):
    """
    Deletes a file or a folder. If it's a folder, it will be deleted even if it's not empty.

    Args:
        path (str): The path to the file or folder to be deleted.
        verbose (bool): Whether to display verbose messages. Defaults to True.
    """
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename
    
    try:
        # Check if the path exists
        if not os.path.exists(path):
            if verbose:
                print(f"Path '{path}' does not exist.")
            return

        # If it's a file, delete it
        if os.path.isfile(path):
            os.remove(path)
            if verbose:
                print(f"File '{path}' deleted successfully.")

        # If it's a directory, delete it
        elif os.path.isdir(path):
            shutil.rmtree(path)
            if verbose:
                print(f"Folder '{path}' deleted successfully.")

    except Exception as e:
        HandleError(str(e), caller_filename, caller_line)

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
    """
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename
    try:

        
        if mode == "f":
            if os.path.exists(path):
                if verbose:
                    print(f"Info: The folder '{path}' already exists. Deleting and recreating.")
                shutil.rmtree(path)
            os.makedirs(path, exist_ok=True)
        elif mode == "o":
            if os.path.exists(path):
                if verbose:
                    print(f"Info: The folder '{path}' already exists. Overwriting.")
                shutil.rmtree(path)
            os.makedirs(path, exist_ok=True)
        elif mode == "c":
            if not os.path.exists(path):
                if verbose:
                    print(f"Info: The folder '{path}' doesn't exist. Creating it.")
                os.makedirs(path)
            else:
                if verbose:
                    print(f"Info: The folder '{path}' already exists. Skipping creation.")
                    
        elif mode == "a":
            if os.path.exists(path):
                user_input = input(f"The folder '{path}' already exists. Do you want to delete and overwrite it? (y/n): ")
                if user_input.lower() == "y":
                    if verbose:
                        print(f"Info: The folder '{path}' already exists. Deleting and recreating.")
                    shutil.rmtree(path)
                    os.makedirs(path, exist_ok=True)
                else:
                    print("Folder creation aborted.")
            else:
                os.makedirs(path, exist_ok=True)
        else:
            msg=f"Invalid mode '{mode}'. Please use 'f' (force_create), 'o' (overwrite), 'c' (create_if_not_exist), or 'a' (ask_user)."
            HandleError(msg,caller_filename, caller_line)

    except PermissionError as pe:
        msg=f"Error: Permission denied to create the folder '{path}' (Occurred in {caller_filename}, line {caller_line})"
        HandleError(msg,caller_filename, caller_line)
    except Exception as e:
        msg=f"Error: {str(e)} (Occurred in {caller_filename}, line {caller_line})"
        HandleError(msg,caller_filename, caller_line)

file_pointers = {}

def save_file_pointer(file_path, offset):
    file_pointers[file_path] = offset

def get_file_pointer(file_path):
    return file_pointers.get(file_path, 0)

def ReadFile(file_path):
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename    
    try:
        if not os.path.exists(file_path):
            msg=f"File not found: {file_path}"
            HandleError(msg,caller_filename, caller_line)

        offset = get_file_pointer(file_path)
        with open(file_path, 'r') as file:
            file.seek(offset)
            line = file.readline()
            if not line:
                return None

            # Strip various newline characters (\n, \r, \r\n)
            line = line.rstrip('\n').rstrip('\r')
            save_file_pointer(file_path, file.tell())
            return line

    except PermissionError as pe:
        msg=f"Error: Permission denied to read the file '{file_path}' (Occurred in {caller_filename}, line {caller_line})"
        HandleError(msg,caller_filename, caller_line)
    except FileNotFoundError as fe:
        msg=f"Error: {str(fe)} (Occurred in {caller_filename}, line {caller_line})"
        HandleError(msg,caller_filename, caller_line)
    except Exception as e:
        msg=f"Error: {str(e)} (Occurred in {caller_filename}, line {caller_line})"
        HandleError(msg,caller_filename, caller_line)

def save_file_pointer(file_path, offset):
    file_pointers[file_path] = offset

def get_file_pointer(file_path):
    return file_pointers.get(file_path, 0)

def WriteFile(file_path, lines):
    """
    Write lines to a file in either append or write mode based on the file pointer.

    Args:
        file_path (str): The path to the file to be written.
        lines (str or list of str): The lines to be written to the file.

    Returns:
        None
    """
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename       
    try:

        offset = get_file_pointer(file_path)

        if offset == 0:
            mode = "w"  # If the file pointer is at the beginning, use write mode
        else:
            mode = "a+"  # If the file pointer is not at the beginning, use append and read mode

        with open(file_path, mode) as file:
            # Move the file pointer to the end of the file
            file.seek(0, os.SEEK_END)

            if isinstance(lines, str):
                file.write(lines)
            elif isinstance(lines, list):
                file.writelines(lines)

            # Update the file pointer to the end of the file
            save_file_pointer(file_path, file.tell())

    except Exception as e:
        msg=f"{e}"
        HandleError(msg,caller_filename, caller_line)




def ReadImage(image_path, mode='RGB', method='auto'):

    """
    Read an image from the specified file path.

    Args:
        image_path (str): The path to the image file.
        mode (str): The desired mode for loading the image ('RGB', 'L', etc.). Defaults to 'RGB'.
        method (str): The method to use for loading the image ('auto', 'PIL', or 'CV2'). Defaults to 'auto'.

    Returns:
        PIL.Image.Image or numpy.ndarray: The loaded image.
    """

    try:
        caller_frame = inspect.currentframe().f_back
        caller_filename = caller_frame.f_globals.get('__file__')
        caller_line = caller_frame.f_lineno    
        
        # Check if mode is valid
        if mode not in ['RGB', 'L']:
            msg = "Invalid mode. Please use 'RGB' or 'L'."
            HandleError(msg, caller_filename, caller_line)
                
        # Determine the appropriate method for image loading (PIL or CV2) based on file extension
        if method == 'auto':
            _, file_extension = os.path.splitext(image_path)
            if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']:
                method = 'PIL'
            else:
                method = 'CV2'

        # Load image using PIL (Pillow)
        if method == 'PIL':
            img = Image.open(image_path)
            # Convert grayscale image to RGB if specified
            if img.mode == 'L' and mode == 'RGB':
                img = img.convert('RGB')
        
        # Load image using OpenCV (cv2)
        elif method == 'CV2':
            img = cv2.imread(image_path)
            if img is None:
                msg=f"File not found or unsupported format: {image_path}"
                HandleError(msg,caller_filename, caller_line)

            # Handle grayscale and color conversions using OpenCV
            if len(img.shape) == 2 or (len(img.shape) == 3 and img.shape[2] == 1):
                if mode == 'RGB':
                    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            else:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Raise error for unsupported methods
        else:
            msg=f"Unsupported method: {method}. Please use 'auto', 'PIL', or 'CV2'."
            HandleError(msg,caller_filename, caller_line)

        return img

    except PermissionError as pe:
        msg=f"Error: Permission denied to open - {image_path}"
        HandleError(msg,caller_filename, caller_line)
        exit(0)

    except FileNotFoundError as e:
        msg=f"Error: {str(e)}"
        HandleError(msg,caller_filename, caller_line)
        exit(0)

    except Exception as e:        
        msg=f"Error reading the image: {str(e)})"
        HandleError(msg,caller_filename, caller_line)
        exit(0)

    return None




def SaveImage(image, save_path, method='auto'):
    save_path = os.path.abspath(save_path)

    caller_frame = inspect.currentframe().f_back
    caller_filename = caller_frame.f_globals.get('__file__')
    caller_line = caller_frame.f_lineno 
    try:
        if method == 'auto':
            if isinstance(image, Image.Image):
                method = 'PIL'
            elif isinstance(image, np.ndarray):
                method = 'CV2'
            else:
                msg=f"Unsupported image type for automatic saving method detection."
                HandleError(msg,caller_filename, caller_line)


        if method == 'PIL':
            if isinstance(image, Image.Image):
                image.save(save_path)
            else:
                msg="Unsupported image type. Please provide a PIL Image."
                HandleError(msg,caller_filename, caller_line)

        elif method == 'CV2':
            if isinstance(image, np.ndarray):
                # Check if the user has write permission to the save_path
                if not os.access(os.path.dirname(save_path), os.W_OK):
                    
                    msg= f"Permission denied to save the image to {save_path}"
                    HandleError(msg,caller_filename, caller_line)
                cv2.imwrite(save_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
            else:
                msg="Unsupported image type. Please provide a numpy array (cv2 image)."
                HandleError(msg,caller_filename, caller_line)

        else:
            msg=f"Unsupported method: {method}. Please use 'auto', 'PIL', or 'CV2'."
            HandleError(msg,caller_filename, caller_line)

        return True  # Image saved successfully
    except PermissionError as pe:
        msg=f"PermissionError: {str(pe)}"
        HandleError(msg,caller_filename, caller_line)

        return False
    except ValueError as ve:
        msg=f"ValueError: {str(ve)}"
        HandleError(msg,caller_filename, caller_line)
        return False
    except Exception as e:
        msg=f"Error saving the image: {str(e)}"
        HandleError(msg,caller_filename, caller_line)
        return False



def HandleError(msg, caller_filename, caller_line):
    
    print(f"[Error: {caller_filename}, line {caller_line}] " + msg)
    exit(0)
    


def ConvertToGrayscale(image, method='auto'):
    """
    Convert an image to grayscale.

    Args:
        image (PIL.Image.Image or numpy.ndarray): The input image.
        method (str): The method to use for converting the image ('auto', 'PIL', or 'CV2').
                      Defaults to 'auto' which automatically detects the input type.

    Returns:
        PIL.Image.Image or numpy.ndarray: The grayscale image.

    Raises:
        ValueError: If an unsupported method is specified.

    Example:
        # Convert an image to grayscale using the default 'auto' method
        grayscale_image = ConvertToGrayscale(image)

        # Convert an image to grayscale using the 'PIL' method
        grayscale_image = ConvertToGrayscale(image, method='PIL')

        # Convert an image to grayscale using the 'CV2' method
        grayscale_image = ConvertToGrayscale(image, method='CV2')
    """
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename        
    try:
        caller_frame = inspect.currentframe().f_back
        caller_filename = caller_frame.f_globals.get('__file__')
        caller_line = caller_frame.f_lineno    
        if method == 'auto':
            if isinstance(image, Image.Image):
                return image.convert('L')
            elif isinstance(image, np.ndarray):
                if len(image.shape) == 2:
                    return image
                elif len(image.shape) == 3 and image.shape[2] == 3:
                    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
                else:
                    msg="Unsupported image format for automatic conversion to grayscale."
                    HandleError(msg,caller_filename, caller_line)
            else:
                msg="Unsupported image type. Please provide a PIL Image or numpy array (cv2 image)."
                HandleError(msg,caller_filename, caller_line)
        elif method == 'PIL':
            if isinstance(image, Image.Image):
                return image.convert('L')
            else:
                msg="Unsupported image type for 'PIL' method. Please provide a PIL Image."
                HandleError(msg,caller_filename, caller_line)
        elif method == 'CV2':
            if isinstance(image, np.ndarray):
                if len(image.shape) == 2:
                    return image
                elif len(image.shape) == 3 and image.shape[2] == 3:
                    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
                else:
                    msg="Unsupported image format for 'CV2' conversion to grayscale."
                    HandleError(msg,caller_filename, caller_line)
            else:
                msg="Unsupported image type for 'CV2' method. Please provide a numpy array (cv2 image)."
                HandleError(msg,caller_filename, caller_line)
        else:
            msg=f"Unsupported method: {method}. Please use 'auto', 'PIL', or 'CV2'."
            HandleError(msg,caller_filename, caller_line)
    except Exception as e:
        msg=f"Error converting to grayscale: {str(e)}"
        HandleError(msg,caller_filename, caller_line)
        return None

def ConvertToRGB(image, method='auto'):
    """
    Convert an image to RGB color mode.

    Args:
        image (PIL.Image.Image or numpy.ndarray): The input image.
        method (str): The method to use for conversion ('auto', 'PIL', or 'CV2').
                      Defaults to 'auto' which automatically detects the input type.

    Returns:
        PIL.Image.Image or numpy.ndarray: The image converted to RGB color mode.

    Raises:
        ValueError: If an unsupported method is specified.

    Example:
        # Convert an image to RGB color mode using the default 'auto' method
        rgb_image = ConvertToRGB(image)

        # Convert an image to RGB color mode using the 'PIL' method
        rgb_image = ConvertToRGB(image, method='PIL')

        # Convert an image to RGB color mode using the 'CV2' method
        rgb_image = ConvertToRGB(image, method='CV2')
    """
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename        
    try:
        if method == 'auto':
            if isinstance(image, Image.Image):
                if image.mode == 'L':
                    return image.convert('RGB')
                elif image.mode == 'RGB':
                    return image
                else:
                    msg="Unsupported image mode for automatic conversion to RGB."
                    HandleError(msg,caller_filename, caller_line)
            elif isinstance(image, np.ndarray):
                if len(image.shape) == 2:
                    msg="Cannot convert a grayscale image with 'auto' method."
                    HandleError(msg,caller_filename, caller_line)
                elif len(image.shape) == 3 and image.shape[2] == 3:
                    return image
                elif len(image.shape) == 3 and image.shape[2] == 1:
                    return cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
                else:
                    msg="Unsupported image format for automatic conversion to RGB."
                    HandleError(msg,caller_filename, caller_line)
            else:
                msg="Unsupported image type. Please provide a PIL Image or numpy array (cv2 image)."
                HandleError(msg,caller_filename, caller_line)
        elif method == 'PIL':
            if isinstance(image, Image.Image):
                if image.mode == 'L':
                    return image.convert('RGB')
                elif image.mode == 'RGB':
                    return image
                else:
                    msg="Unsupported image mode for 'PIL' conversion to RGB."
                    HandleError(msg,caller_filename, caller_line)
            else:
                msg="Unsupported image type for 'PIL' method. Please provide a PIL Image."
                HandleError(msg,caller_filename, caller_line)
        elif method == 'CV2':
            if isinstance(image, np.ndarray):
                if len(image.shape) == 2:
                    msg="Cannot convert a grayscale image with 'CV2' method."
                    HandleError(msg,caller_filename, caller_line)
                elif len(image.shape) == 3 and image.shape[2] == 3:
                    return image
                elif len(image.shape) == 3 and image.shape[2] == 1:
                    return cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
                else:
                    msg="Unsupported image format for 'CV2' conversion to RGB."
                    HandleError(msg,caller_filename, caller_line)
            else:
                msg="Unsupported image type for 'CV2' method. Please provide a numpy array (cv2 image)."
                HandleError(msg,caller_filename, caller_line)
        else:
            msg=f"Unsupported method: {method}. Please use 'auto', 'PIL', or 'CV2'."
            HandleError(msg,caller_filename, caller_line)
    except Exception as e:
        msg=f"Error converting the image to RGB: {str(e)}"
        HandleError(msg,caller_filename, caller_line)
        return None

def CropImage(image, coordinates):
    """
    Crop an image.

    Args:
        image (PIL.Image.Image): The input image.
        coordinates (list): A list containing the left, top, right, and bottom coordinates.

    Returns:
        PIL.Image.Image: The cropped image.

    Example:
        # Crop a region of interest from an image
        cropped_image = CropImage(image, [0, 0, 50, 50])
    """
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename        
    try:
        if isinstance(image, Image.Image):
            if len(coordinates) == 4:
                left, top, right, bottom = coordinates
                return image.crop((left, top, right, bottom))
            else:
                msg="Coordinates list should contain exactly 4 values."
                HandleError(msg,caller_filename, caller_line)
        else:
            msg="Unsupported image type. Please provide a PIL Image."
            HandleError(msg,caller_filename, caller_line)
    except Exception as e:        
        msg=f"Error cropping the image: {str(e)}"
        HandleError(msg,caller_filename, caller_line)
        return None


def GetImageSize(image, method='auto'):
    """
    Get the size (width, height) and number of channels of an image using either PIL (Pillow) or OpenCV (cv2).

    Args:
        image (PIL.Image.Image or numpy.ndarray): The image to get the size and channels from.
        method (str): The method to use for reading the image ('auto', 'PIL' for Pillow, 'CV2' for OpenCV).
                      Defaults to 'auto'.

    Returns:
        tuple: A tuple containing the width, height, and number of channels of the image, e.g., (width, height, channels).
               If the image method is unsupported, returns (0, 0, 0).
    """
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename        
    try:
        if method == 'auto':
            if isinstance(image, Image.Image):
                # Get the size (width and height) of the image
                width, height = image.size
                # Get the number of channels (always 3 for RGB images)
                channels = 3
            elif isinstance(image, np.ndarray):
                # Get the size (width and height) of the image
                height, width, channels = image.shape
            else:
                msg="Unsupported image type for automatic detection."
                HandleError(msg,caller_filename, caller_line)
        elif method == 'PIL':
            if isinstance(image, Image.Image):
                # Get the size (width and height) of the image
                width, height = image.size
                # Get the number of channels (always 3 for RGB images)
                channels = 3
            else:
                msg="Unsupported image type for 'PIL' method. Please provide a PIL Image."
                HandleError(msg,caller_filename, caller_line)
        elif method == 'CV2':
            if isinstance(image, np.ndarray):
                # Get the size (width and height) of the image
                height, width, channels = image.shape
            else:
                msg="Unsupported image type for 'CV2' method. Please provide a numpy array (cv2 image)."
                HandleError(msg,caller_filename, caller_line)
        else:
            msg=f"Unsupported method: {method}. Please use 'auto', 'PIL', or 'CV2'."
            HandleError(msg,caller_filename, caller_line)

        return width, height, channels

    except Exception as e:
        msg=f"Error: {str(e)}"
        HandleError(msg,caller_filename, caller_line)
        return 0, 0, 0




def ResizeImage(image, size, verbose=True):
    """
    Resize an image to the specified size while preserving the aspect ratio.

    Args:
        image (PIL.Image.Image): The input image.
        size (tuple): The target size (width, height).
        verbose (bool): Whether to display verbose messages. Defaults to True.

    Returns:
        PIL.Image.Image: The resized image.
    """
    print("Here")
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename         
    try:
        if not isinstance(image, Image.Image):
            msg="Input 'image' must be a PIL Image object."
            HandleError(msg,caller_filename, caller_line)
        
        if not isinstance(size, tuple) or len(size) != 2:
            msg="Input 'size' must be a tuple of two integers (width, height)."
            HandleError(msg,caller_filename, caller_line)
        
        if verbose:
            print(f"Resizing image to {size}...")
        
        resized_image = image.resize(size, Image.ANTIALIAS)
        return resized_image
    except Exception as e:
        msg=f"{e}"
        HandleError(msg,caller_filename, caller_line)
        
        exit(1)


def GaussianBlurImage(image, sigma=1.0, verbose=True):
    """
    Apply Gaussian blur to an image.

    Args:
        image (PIL.Image.Image): The input image.
        sigma (float): The standard deviation of the Gaussian kernel.
        verbose (bool): Whether to display verbose messages. Defaults to True.

    Returns:
        PIL.Image.Image: The blurred image.
    """
    
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename         
    try:
        if not isinstance(image, Image.Image):
            msg="Input 'image' must be a PIL Image object."
        
        if not isinstance(sigma, (int, float)) or sigma <= 0:
            msg="Input 'sigma' must be a positive number."
            HandleError(msg,caller_filename, caller_line)
        
        if verbose:
            print(f"Applying Gaussian blur with sigma={sigma}...")
        
        blurred_image = image.filter(ImageFilter.GaussianBlur(sigma))
        return blurred_image
    except Exception as e:
        msg=f"{e}"
        HandleError(msg,caller_filename, caller_line)
        
        exit(1)


def ConvertImageToGrayscale(image, verbose=True):
    """
    Convert an image to grayscale.

    Args:
        image (PIL.Image.Image): The input image.
        verbose (bool): Whether to display verbose messages. Defaults to True.

    Returns:
        PIL.Image.Image: The grayscale image.
    """
    
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename         
    try:
        if not isinstance(image, Image.Image):
            msg="Input 'image' must be a PIL Image object."
            HandleError(msg,caller_filename, caller_line)
        
        if verbose:
            print("Converting image to grayscale...")
        
        grayscale_image = image.convert("L")
        return grayscale_image
    except Exception as e:
        msg=f"{e}"
        HandleError(msg,caller_filename, caller_line)        
        exit(1)


def SharpenImage(image, factor=2.0, verbose=True):
    """
    Sharpen an image.

    Args:
        image (PIL.Image.Image): The input image.
        factor (float): The sharpening factor.
        verbose (bool): Whether to display verbose messages. Defaults to True.

    Returns:
        PIL.Image.Image: The sharpened image.
    """
    
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename         
    try:
        if not isinstance(image, Image.Image):
            msg="Input 'image' must be a PIL Image object."
            HandleError(msg,caller_filename, caller_line)
        
        if not isinstance(factor, (int, float)) or factor <= 0:
            msg="Input 'factor' must be a positive number."
            HandleError(msg,caller_filename, caller_line)
        
        if verbose:
            print(f"Sharpening image with factor={factor}...")
        
        enhancer = ImageEnhance.Sharpness(image)
        sharpened_image = enhancer.enhance(factor)
        return sharpened_image
    except Exception as e:
        msg=f"{e}"
        HandleError(msg,caller_filename, caller_line)          
        

def DetectEdgesInImage(image, method='canny', threshold1=100, threshold2=200, verbose=True):
    """
    Detect edges in an image using various edge detection methods.

    Args:
        image (PIL.Image.Image): The input image.
        method (str): The edge detection method to use ('canny', 'sobel', 'laplacian', 'prewitt', or 'scharr').
        threshold1 (int): The first threshold for the hysteresis procedure (only for 'canny' method).
        threshold2 (int): The second threshold for the hysteresis procedure (only for 'canny' method).
        verbose (bool): Whether to display verbose messages. Defaults to True.

    Returns:
        PIL.Image.Image: The edge-detected image.
    """
    caller_frame = sys._getframe(1)
    caller_line = caller_frame.f_lineno
    caller_filename = caller_frame.f_globals.get('__file__')

    try:
        if not isinstance(image, Image.Image):
            msg = "Input 'image' must be a PIL Image object."
            HandleError(msg, caller_filename, caller_line)

        if method == 'canny':
            if not isinstance(threshold1, int) or not isinstance(threshold2, int) or threshold1 >= threshold2:
                msg = "For 'canny' method, input thresholds must be integers, and threshold1 must be less than threshold2."
                HandleError(msg, caller_filename, caller_line)

            if verbose:
                print(f"Detecting edges in image using Canny edge detection (threshold1={threshold1}, threshold2={threshold2})...")

            # Convert the input image to grayscale
            image = image.convert('L')
            image_array = np.array(image)
            edges = cv2.Canny(image_array, threshold1, threshold2)
            edge_image = Image.fromarray(edges)
            return edge_image

        elif method == 'sobel' or method == 'laplacian' or method == 'prewitt' or method == 'scharr':
            if verbose:
                print(f"Detecting edges in image using {method.capitalize()} edge detection...")
            
            # Convert the input image to a NumPy array
            image_array = np.array(image)

            # Convert the image to grayscale if it's not already
            if len(image_array.shape) == 3 and image_array.shape[2] == 3:
                image_array = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)

            if method == 'sobel':
                edges = cv2.Sobel(image_array, cv2.CV_64F, 1, 1)
            elif method == 'laplacian':
                edges = cv2.Laplacian(image_array, cv2.CV_64F)
            elif method == 'prewitt':
                kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
                kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
                gradient_x = cv2.filter2D(image_array, -1, kernel_x)
                gradient_y = cv2.filter2D(image_array, -1, kernel_y)
                edges = np.sqrt(gradient_x**2 + gradient_y**2)
            elif method == 'scharr':
                gradient_x = cv2.Scharr(image_array, cv2.CV_64F, 1, 0)
                gradient_y = cv2.Scharr(image_array, cv2.CV_64F, 0, 1)
                edges = np.sqrt(gradient_x**2 + gradient_y**2)

            edge_image = Image.fromarray(edges.astype('uint8'))
            return edge_image

        else:
            msg = f"Unsupported edge detection method: {method}. Please use 'canny', 'sobel', 'laplacian', 'prewitt', or 'scharr'."
            HandleError(msg, caller_filename, caller_line)

    except Exception as e:
        msg = f"{e}"
        HandleError(msg, caller_filename, caller_line)

def ConvolveImage(image, kernel, verbose=True):
    """
    Apply convolution to an image with a given kernel.

    Args:
        image (PIL.Image.Image): The input image.
        kernel (numpy.ndarray): The convolution kernel.
        verbose (bool): Whether to display verbose messages. Defaults to True.

    Returns:
        PIL.Image.Image: The convolved image.
    """
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename         
    try:
        if not isinstance(image, Image.Image):
            msg="Input 'image' must be a PIL Image object."
            HandleError(msg,caller_filename, caller_line)
        
        if not isinstance(kernel, np.ndarray) or len(kernel.shape) != 2:
            msg="Input 'kernel' must be a 2D NumPy array."
            HandleError(msg,caller_filename, caller_line)
        
        if verbose:
            print("Applying convolution to image...")
        
        image_array = np.array(image)
        convolved_image = convolve2d(image_array, kernel, mode='same', boundary='wrap')
        convolved_image = Image.fromarray(convolved_image)
        return convolved_image
    except Exception as e:
        msg=f"{e}"
        HandleError(msg,caller_filename, caller_line)          
        exit(1)



def ApplyFilter(image, kernel):
    """
    Apply a convolution filter to an image using a custom kernel.

    Args:
        image (PIL.Image.Image or numpy.ndarray): The input image to apply the filter to.
        kernel (numpy.ndarray): The custom convolution kernel.

    Returns:
        PIL.Image.Image or numpy.ndarray: The filtered image.
    """
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename         
    try:
        if isinstance(image, Image.Image):
            # If the input image is a PIL Image, convert it to a numpy array
            image = np.array(image)

        if isinstance(image, np.ndarray):
            # If the input image is a numpy array (cv2 image)
            filtered_image = cv2.filter2D(image, -1, kernel)

            if len(filtered_image.shape) == 2:
                # Convert grayscale image back to PIL Image
                filtered_image = Image.fromarray(filtered_image)
                return filtered_image

            return filtered_image

        msg="Unsupported image type. Please provide a PIL Image or numpy array (cv2 image)."
        HandleError(msg,caller_filename, caller_line)

    except Exception as e:
        msg=f"Error applying the filter: {str(e)}"
        HandleError(msg,caller_filename, caller_line)



def ShowImage(image, title="Image", verbose=True):
    """
    Display an image using matplotlib.

    Args:
        image (PIL.Image.Image): The input image.
        title (str): The title of the displayed image.
        verbose (bool): Whether to display verbose messages. Defaults to True.

    Returns:
        None
    """
    caller_frame = sys._getframe(1)  # Get the caller's frame (1 level up in the call stack)
    caller_line = caller_frame.f_lineno  # Get the caller's line number
    caller_filename = caller_frame.f_globals.get('__file__')  # Get the caller's filename         
    try:
        if not isinstance(image, Image.Image):
            msg="Input 'image' must be a PIL Image object."
        
        if verbose:
            print("Displaying image...")
        
        plt.figure(figsize=(8, 8))
        plt.imshow(image, cmap='gray')
        plt.title(title)
        plt.axis('off')
        plt.show()
    except Exception as e:
        msg=f"{e}"
        HandleError(msg,caller_filename, caller_line)          
        
        exit(1)

def CV2PIL(cv2_image):
    """
    Convert an OpenCV image (BGR format) to a PIL Image (RGB format).

    Args:
        cv2_image (numpy.ndarray): The OpenCV image.

    Returns:
        PIL.Image.Image or None: The PIL Image if conversion is successful, None otherwise.
    """
    caller_frame = sys._getframe(1)
    caller_line = caller_frame.f_lineno
    caller_filename = caller_frame.f_globals.get('__file__')

    try:
        if cv2_image is None:
            return None
        return Image.fromarray(cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB))
    except Exception as e:
        msg = f"Error converting from OpenCV to PIL: {str(e)}"
        HandleError(msg, caller_filename, caller_line)
        return None

def PIL2CV2(pil_image):
    """
    Convert a PIL Image (RGB format) to an OpenCV image (BGR format).

    Args:
        pil_image (PIL.Image.Image): The PIL Image.

    Returns:
        numpy.ndarray or None: The OpenCV image if conversion is successful, None otherwise.
    """
    caller_frame = sys._getframe(1)
    caller_line = caller_frame.f_lineno
    caller_filename = caller_frame.f_globals.get('__file__')

    try:
        if pil_image is None:
            return None
        return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    except Exception as e:
        msg = f"Error converting from PIL to OpenCV: {str(e)}"
        HandleError(msg, caller_filename, caller_line)
        return None

