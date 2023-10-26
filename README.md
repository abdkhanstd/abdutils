# abdutils

# abdutils: Simplifying Python File Operations

Are you tired of dealing with complex Python libraries and struggling with unclear learning examples? We've been there too, which is why we created `abdutils`.

## What is abdutils?

`abdutils` is a Python utility module that aims to simplify common file and folder operations, making Python programming more efficient and intuitive. We understand that Python libraries can sometimes feel overly complicated, and learning from existing examples can be challenging. That's why we're building `abdutils` to provide a straightforward and user-friendly solution.

## Why Choose abdutils?

- **Simplicity**: We believe in keeping things simple. `abdutils` offers easy-to-use functions for various file-related tasks, eliminating the need to reinvent the wheel when working with files and directories.

- **Clarity**: Our code and documentation are designed with clarity in mind. We want you to understand how everything works, making your Python development experience smoother.

- **Open to Suggestions**: We value your input! If you have suggestions, ideas, or improvements to make `abdutils` even better, please don't hesitate to [open an issue](https://github.com/abdkhanstd/abdutils/issues) or submit a [pull request](https://github.com/abdkhanstd/abdutils/pulls).

## Getting Started

To get started with `abdutils`, you can install it easily using `pip`. Here's how:

```bash
pip install git+https://github.com/abdkhanstd/abdutils.git
```
## Purpose

- **Ease of Programming:** `abdutils` strives to streamline Python programming by providing a collection of utility functions, which currently encompass fundamental file and directory operations.

- **Enhanced File Handling:** It provides tools to perform file creation, reading, and writing tasks effortlessly.

- **Time-Saving:** By using `abdutils`, you can save time on routine file operations, allowing you to focus on the core aspects of your projects.

Whether you're a beginner or an experienced developer, `abdutils` is here to make your Python coding experience smoother and more enjoyable.

## Installation

You can install `abdutils` directly from its GitHub repository using pip:

```bash
pip install git+https://github.com/abdkhanstd/abdutils.git
```

To verify the installation of a Python package installed via `pip` and to provide installation instructions in a GitHub README file, follow these steps:

## Verifying Installation

1. Open your terminal or command prompt.

2. Run the following command to verify if the package "abdutils" has been installed successfully:

   ```
   pip show abdutils
   ```

   This command will display information about the installed package, including its version, location, and other details. If the package is installed correctly, you'll see its information. If it's not installed, you'll receive an error message.

## Installation (Build from repository)

To install the `abdutils` package, you can use `pip`. Run the following command in your terminal or command prompt:

   ```bash
   pip install git+https://github.com/abdkhanstd/abdutils.git
   ```

   This will install the latest version of the package directly from the GitHub repository.

   If you prefer to install manually, you can follow these steps:

   1. Clone the GitHub repository:

      ```bash
      git clone https://github.com/abdkhanstd/abdutils.git
      ```

   2. Change your current directory to the cloned repository:

      ```bash
      cd abdutils
      ```

   3. Install the package using `pip`:

      ```bash
      pip install .
      ```


## Table of Contents

- [CreateFolder](#createfolder)
- [ReadFile](#readfile)
- [WriteFile](#writefile)

## CreateFolder

The `CreateFolder` function allows you to create folders with various modes.

### Function Signature

```python
CreateFolder(path, mode="a", verbose=True)
```

- `path` (str): The path to the folder to be created.
- `mode` (str): The mode for folder creation ('f', 'o', 'c', or 'a'). Defaults to 'a' (ask_user).
- `verbose` (bool): Whether to display verbose messages. Defaults to True.

#### Examples

##### Example 1: Create a folder using the default "ask_user" mode with verbose messages

```python
import abdutils as abd

abd.CreateFolder("my_folder", verbose=True)
# Expected Output: Info: The folder 'my_folder' already exists. Deleting and recreating.
```

##### Example 2: Create a folder recursively with a long path without verbose messages

```python
import abdutils as abd

abd.CreateFolder("parent/child/grandchild", verbose=False)
# No output if the folder doesn't exist; Info message if the folder already exists.
```

##### Example 3: Force create a folder, displaying a message

```python
import abdutils as abd

abd.CreateFolder("folder_to_force_create", mode="f", verbose=True)
# Expected Output: Info: The folder 'folder_to_force_create' already exists. Deleting and recreating.
```

##### Example 4: Overwrite a folder, displaying a message

```python
import abdutils as abd

abd.CreateFolder("folder_to_overwrite", mode="o", verbose=True)
# Expected Output: Info: The folder 'folder_to_overwrite' already exists. Overwriting.
```

##### Example 5: Create a folder if it doesn't exist, displaying a message

```python
import abdutils as abd

abd.CreateFolder("folder_to_create_if_not_exist", mode="c", verbose=True)
# Expected Output: Info: The folder 'folder_to_create_if_not_exist' already exists. Skipping creation.
```

##### Example 6: Ask the user whether to delete and recreate a folder, displaying a message

```python
import abdutils as abd

abd.CreateFolder("folder_to_ask_user", mode="a", verbose=True)
# User will be prompted for input.
```

## ReadFile

The `ReadFile` function allows you to read a file line by line and return one line at a time with each function call.

### Function Signature

```python
ReadFile(file_path)
```

- `file_path` (str): The path to the file to be read.

#### Examples

##### Example 1: Read a file line by line

```python
import abdutils as abd

line1 = abd.ReadFile("sample.txt")
print(line1)
# Expected Output: Contents of the first line in 'sample.txt'
```

##### Example 2: Read multiple lines

```python
import abdutils as abd

line1 = abd.ReadFile("sample.txt")
line2 = abd.ReadFile("sample.txt")
print(line1)
print(line2)
# Expected Output: Contents of the first and second lines in 'sample.txt'
```

##### Example 3: Import and use `ReadFile`

```python
from abdutils import ReadFile

line1 = ReadFile("imported_file.txt")
print(line1)
# Expected Output: Contents of the first line in 'imported_file.txt'
```

##### Example 4: Read Lines in a Loop (while)

```python
import abdutils as abd

file_path = "sample.txt"
line = abd.ReadFile(file_path)

while line:
    print(line)
    line = abd.ReadFile(file_path)
# Reads and prints all lines of 'sample.txt' using a while loop.
```

##### Example 5: Read Lines in a Loop (for)

```python
import abdutils as abd

file_path = "sample.txt"
for line in abd.ReadFile(file_path):
    print(line)
# Reads and prints all lines of 'sample.txt' using a for loop.
```

## WriteFile

The `WriteFile` function enables you to write lines to a file in either append or write mode.

### Function Signature

```python
WriteFile(file_path, line)
```

- `file_path` (str): The path to the file to be written.
- `line` (str): The line to be written to the file.

#### Examples

##### Example 1: Write a line to a file

```python
import abdutils as abd

abd.WriteFile("my.txt", "Hello, World!")
# The line "Hello, World!" is written to 'my.txt'
```

##### Example 2: Write multiple lines to a file

```python
import abdutils as abd

lines_to_write = ["Line 1", "Line 2", "Line 3"]
abd.WriteFile("my.txt", lines_to_write)
# The lines "Line 1", "Line 2", and "Line 3" are appended to 'my.txt'
```

##### Example 3: Import and use `WriteFile`

```python
from abdutils import WriteFile

WriteFile("imported_file.txt", "This is an imported file.")
# The line "This is an imported file." is written to 'imported_file.txt'
```

##### Example 4: Write Lines in a Loop (for)

```python
import abdutils as abd

lines_to_write = ["Line 1", "Line 2", "Line 3"]
for line in lines_to_write:
    abd.WriteFile("looped_file.txt", line, mode="a")
# Overwrites the file 'looped_file.txt' with each line.

```

##### Example 5: Write Lines in a Loop (while)

```python
import abdutils as abd

line_to_write = "Looped line"
counter = 0
while counter < 3:
    abd.WriteFile("looped_file.txt", line_to_write, 'a')
    counter += 1
# Writes "Looped line" to 'looped_file.txt' three times in append mode.
```
