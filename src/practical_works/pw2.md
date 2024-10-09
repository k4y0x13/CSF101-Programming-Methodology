# Practical Work II

# Practical 2: Text File Analyzer

**Due Date:** 

**Submission:** GitHub repository link containing:
- Python source code (.py file)
- Lab report in markdown format
- Sample text files used for testing

## Learning Objectives
- Implement file handling operations in Python
- Use control structures (loops and conditionals)
- Practice string manipulation
- Implement basic statistical calculations
- Apply error handling techniques

## Requirements
Create a Python program that analyzes a text file and calculates the following statistics:
1. Total number of characters (including spaces and special characters)
2. Total number of words
3. Total number of lines
4. Average word length
5. Most frequent word
6. Number of sentences
7. Word frequency distribution (top 10 words)

## Step-by-Step Implementation Guide

### Step 1: File Input and Basic Structure
1. Create a new Python file named `text_analyzer.py`
2. Implement a function to read the text file:
   ```python
   def read_file(filename):
       try:
           with open(filename, 'r') as file:
               return file.read()
       except FileNotFoundError:
           print(f"Error: File '{filename}' not found")
           return None
   ```

### Step 2: Character Count Function
1. Implement a function to count total characters:
   ```python
   def count_characters(text):
       return len(text)
   ```

### Step 3: Word Count Function
1. Create a function to count words:
   ```python
   def count_words(text):
       words = text.split()
       return len(words)
   ```

### Step 4: Line Count Function
1. Implement line counting:
   ```python
   def count_lines(text):
       lines = text.splitlines()
       return len(lines)
   ```

### Step 5: Advanced Statistics
1. Implement average word length calculation
2. Create a function to find the most frequent word
3. Add sentence counting functionality
4. Implement word frequency distribution

### Step 6: Main Program Structure
1. Create the main program structure
2. Display the statistics to the user

## Testing Instructions
1. Create at least three different text files for testing:
   - A small file (< 100 words)
   - A medium file (100-1000 words)
   - A large file (> 1000 words)
2. Test your program with each file
3. Verify all statistics are calculated correctly

## Expected Output Format
```
Text File Analysis Report
-----------------------
Filename: sample.txt
Total Characters: XXX
Total Words: XXX
Total Lines: XXX
Average Word Length: XX.XX
Most Frequent Word: "XXXX" (XX occurrences)
Number of Sentences: XX
Top 10 Words:
1. word1 (XX)
2. word2 (XX)
...
```
