# Practical 2: Text File Analyzer

## Objective
In this lab, you will create a Python program that analyzes a text file and calculates various statistics using control structures. This exercise will help you practice file handling, string manipulation, and using loops and conditionals in Python.


## Prerequisites
- Basic knowledge of Python syntax
- Understanding of file operations in Python
- Familiarity with control structures (if statements, loops)

## Lab Steps

### Step 0: Preparation

Create a folder and name it practical4. Download the sample.txt text file from this [link](https://drive.google.com/file/d/1j2MC-RE4UbiPnMsn9ZMtjXqVnlX0rZgA/view?usp=sharing) and save it inside the folder. Create your practical5.py file in the same folder
and continue with the subsequent steps. 

### Step 1: Open and Read a Text File

First, let's create a function to open and read a text file:

```python
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
print(content[:100])  # Print the first 100 characters
```

### Step 2: Count the Number of Lines

Now, let's count the number of lines in the file:

```python
def count_lines(content):
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")
```

### Step 3: Count Words

Next, we'll count the total number of words in the file:

```python
def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")
```

### Step 4: Find the Most Common Word

Let's find the most common word in the text:

```python
from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")
```

### Step 5: Calculate Average Word Length

Now, let's calculate the average word length:

```python
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")
```

### Step 6: Combine Everything into a Main Function

Finally, let's combine all these functions into a main function that analyzes the text file:

```python
def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")

# Run the analysis
analyze_text('sample.txt')
```

## Exercises for Students

1. Modify the program to count the number of unique words in the text.
2. Add a function to find the longest word in the text.
3. Implement a feature to count the occurrences of a specific word (case-insensitive).
4. Create a function to calculate the percentage of words that are longer than the average word length.

## Conclusion

In this lab, you've created a text file analyzer using Python. You've practiced file handling, string manipulation, and using control structures like loops and conditionals. The modular approach we've taken allows for easy expansion and modification of the program.

Remember to test your code with different text files to ensure it works correctly in various scenarios.
