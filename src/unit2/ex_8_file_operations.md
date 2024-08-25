# Exercise

# Python File Operations

These exercises are designed to help you practice working with file operations in Python. Follow each step carefully and try to predict the output before running the code.

**Important:** Be cautious when working with file operations, especially when deleting or overwriting files. Always make sure you're working in the **_correct directory_** and with the intended files.

## File Organization

We'll add a new directory called `file_operations` to your existing file structure. The updated structure will look like this:

```
csf101-python_exercises/
│
├── basics/
│   ├── numbers.py
│   ├── strings.py
│   └── booleans.py
│
├── data_structures/
│   ├── lists.py
│   └── dictionaries.py
│
├── operators/
│   ├── arithmetic.py
│   ├── assignment.py
│   ├── comparison.py
│   ├── logical.py
│   └── bitwise.py
│
├── control_structures/
│   ├── conditionals.py
│   ├── loops.py
│   └── break_continue.py
│
├── functions_and_scope/
│   ├── basic_functions.py
│   ├── parameters_and_returns.py
│   ├── scope.py
│   └── recursion.py
│
└── file_operations/
    ├── text_files.py
    ├── binary_files.py
    └── file_management.py
```

Create a new directory called `file_operations` inside your `csf101-python_exercises` directory.

## Exercise 1: Working with Text Files

File: `file_operations/text_files.py`

Create a new file called `text_files.py` in the `file_operations` directory and complete the following exercises in this file.

1. Write a function that creates a new text file and writes a few lines to it.

   ```python
   def create_and_write_file(filename):
       with open(filename, 'w') as file:
           file.write("This is the first line.\n")
           file.write("This is the second line.\n")
           file.write("This is the third line.\n")

   create_and_write_file('sample.txt')
   print("File created and written successfully.")
   ```

2. Write a function that reads and prints the contents of the file you just created.

   ```python
   def read_and_print_file(filename):
       with open(filename, 'r') as file:
           content = file.read()
           print(content)

   read_and_print_file('sample.txt')
   ```

3. Write a function that appends a new line to an existing file.

   ```python
   def append_to_file(filename, new_line):
       with open(filename, 'a') as file:
           file.write(new_line + "\n")

   append_to_file('sample.txt', "This is an appended line.")
   print("Line appended successfully.")
   read_and_print_file('sample.txt')  # Verify the appended line
   ```

4. Write a function that reads a file line by line and prints each line with its line number.

   ```python
   def print_lines_with_numbers(filename):
       with open(filename, 'r') as file:
           for index, line in enumerate(file, start=1):
               print(f"{index}: {line.strip()}")

   print_lines_with_numbers('sample.txt')
   ```

5. Write a function that counts the number of words in a text file.

   ```python
   def count_words(filename):
       with open(filename, 'r') as file:
           content = file.read()
           words = content.split()
           return len(words)

   word_count = count_words('sample.txt')
   print(f"The file contains {word_count} words.")
   ```

## Exercise 2: Working with Binary Files

File: `file_operations/binary_files.py`

Create a new file called `binary_files.py` in the `file_operations` directory and complete the following exercises in this file.

6. Write a function that creates a binary file containing some bytes.

   ```python
   def create_binary_file(filename):
       data = bytes([0, 1, 2, 3, 4, 5])
       with open(filename, 'wb') as file:
           file.write(data)

   create_binary_file('binary_sample.bin')
   print("Binary file created successfully.")
   ```

7. Write a function that reads and prints the contents of the binary file as bytes.

   ```python
   def read_binary_file(filename):
       with open(filename, 'rb') as file:
           content = file.read()
           print("Binary content:", content)

   read_binary_file('binary_sample.bin')
   ```

8. Write a function that appends bytes to an existing binary file.

   ```python
   def append_to_binary_file(filename, data):
       with open(filename, 'ab') as file:
           file.write(data)

   append_to_binary_file('binary_sample.bin', bytes([6, 7, 8, 9]))
   print("Bytes appended to binary file.")
   read_binary_file('binary_sample.bin')  # Verify the appended bytes
   ```

## Exercise 3: File Management

File: `file_operations/file_management.py`

Create a new file called `file_management.py` in the `file_operations` directory and complete the following exercises in this file.

9. Write a function that checks if a file exists.

   ```python
   import os

   def file_exists(filename):
       return os.path.exists(filename)

   print(f"'sample.txt' exists: {file_exists('sample.txt')}")
   print(f"'nonexistent.txt' exists: {file_exists('nonexistent.txt')}")
   ```

10. Write a function that renames a file.

    ```python
    import os

    def rename_file(old_name, new_name):
        os.rename(old_name, new_name)

    rename_file('sample.txt', 'renamed_sample.txt')
    print("File renamed successfully.")
    print(f"'renamed_sample.txt' exists: {file_exists('renamed_sample.txt')}")
    ```

11. Write a function that deletes a file.

    ```python
    import os

    def delete_file(filename):
        if os.path.exists(filename):
            os.remove(filename)
            print(f"{filename} has been deleted.")
        else:
            print(f"{filename} does not exist.")

    delete_file('binary_sample.bin')
    ```

12. Write a function that creates a new directory.

    ```python
    import os

    def create_directory(directory_name):
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
            print(f"Directory '{directory_name}' created successfully.")
        else:
            print(f"Directory '{directory_name}' already exists.")

    create_directory('new_folder')
    ```

13. Write a function that lists all files in a directory.

    ```python
    import os

    def list_files(directory):
        files = os.listdir(directory)
        for file in files:
            print(file)

    print("Files in the current directory:")
    list_files('.')
    ```

14. Write a function that copies a file from one location to another.

    ```python
    import shutil

    def copy_file(source, destination):
        shutil.copy2(source, destination)
        print(f"File copied from {source} to {destination}")

    copy_file('renamed_sample.txt', 'new_folder/copied_sample.txt')
    ```

15. Write a function that reads a CSV file and prints its contents.

    ```python
    import csv

    def read_csv_file(filename):
        with open(filename, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(', '.join(row))

    # First, create a sample CSV file
    with open('sample.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Name', 'Age', 'City'])
        csv_writer.writerow(['Alice', '30', 'New York'])
        csv_writer.writerow(['Bob', '25', 'Los Angeles'])

    print("Contents of sample.csv:")
    read_csv_file('sample.csv')
    ```

Congratulations!

Remember to run each file separately to see the output of your exercises. You can do this by navigating to the appropriate directory in your terminal and running `python filename.py` (e.g., `python text_files.py`).

**Important:** Be cautious when working with file operations, especially when deleting or overwriting files. Always make sure you're working in the correct directory and with the intended files.
