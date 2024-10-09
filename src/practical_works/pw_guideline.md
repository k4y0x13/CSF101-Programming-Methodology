# Practical_Work Submission Guideline

## Lab Report Format
Your REPORT.md should include:
1. Brief description of your implementation approach
2. Explanation program structure.
3. Design Decisions.
4. Screenshots of your program output with different input files
5. Challenges faced and how you resolved them
6. Learning Outcomes

### 1. Brief Description:
* You need to explain how you implemented your solution in few sentences

Example:
> The program is structured in layers, starting with basic file operations, moving to text processing, and finally to statistical analysis. This approach makes the code easier to test and maintain.

### 2. Programme Structure

You need to explain what each function does.
```plaintext
text_analyzer.py
├── Main Functions:
│   ├── read_file() - Handles file input and error checking
│   ├── analyze_text() - Main orchestrator function
│   └── display_results() - Formats and shows output
├── Analysis Functions:
│   ├── count_basic_stats() - Characters, words, sentences
│   ├── calculate_averages() - Word and sentence length
│   └── analyze_frequency() - Letters and words
└── Helper Functions:
    ├── clean_text() - Text preprocessing
    └── format_number() - Output formatting
```

### 3. Design Decisions

You need to explain why you used a certain data structure or why a certain function.

**Example:**
- Used a dictionary to store results for easy access and organization
- Separated concerns by delegating specific calculations to helper functions
- Implemented error checking for edge cases

### 4. Screenshots 

Attach images of how your programme output looks like with different different text files.

### 5. Challanges you Faced

**Challenge 1: Accurate Sentence Detection**

**Problem**: Simple period detection wasn't accurate due to abbreviations (Mr., Dr., etc.)
**Solution**: Implemented a regex-based approach with abbreviation handling:

```python
def count_sentences(text):
    abbreviations = ['Mr.', 'Mrs.', 'Dr.', 'Ph.D.']
    for abbr in abbreviations:
        text = text.replace(abbr, abbr.replace('.', '@'))
    return len(re.split('[.!?]+', text))
```

### 6. Learning Outcomes

Reflect on what you learnt

Example:

```plaintext
Through this project, I gained an understanding of:
- File handling in Python
- The importance of edge case handling
- Writing code in functions
```
