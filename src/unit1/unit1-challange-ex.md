# Unit 1 Challange Ex

# Fruit Transaction Analysis

In this challenge, you'll work with a file containing fruit transaction data. Your task is to read the file, process the data, and perform some calculations. Follow the steps below to complete the challenge.

## Setup

1. Make sure you're in the `challenge-ex` directory.
2. Create a new file called `ex-ch1.py`.
3. The input file `fruit_transactions.txt` should be in the same directory.

At the end of the challenge, your directory should look like this:

```plaintext
csf101-python_exercises/
│
├── challenge-ex/
    ├── ex-ch1.py                 # Student's solution file
    ├── fruit_transactions.txt    # Input data file
    └── transaction_summary.txt   # Output summary file (created by student's code)
```

## Exercise Steps

1. Open the file:

   - Use the `with` statement to open `fruit_transactions.txt` in read mode.

   Hint: Remember to use the `open()` function and specify the file mode.

2. Read the file contents:

   - Read all lines from the file into a list.

   Hint: You can use the `readlines()` method or a list comprehension.

3. Process the data:

   - For each line in the file:
     a. Split the line into its components (name, action, quantity, item, price).
     b. Convert quantity to an integer and price to a float.
   - Store this processed data in a suitable data structure (e.g., a list of tuples or dictionaries).

   Hint: The `split()` method will be useful here. Don't forget to handle the newline character.

4. Calculate total sales:

   - Sum up the total value of all "sold" transactions.
   - Print the result.

   Hint: You'll need to use a loop and an if statement to check the action.

5. Find the most popular fruit:

   - Determine which fruit was involved in the most transactions (regardless of action).
   - Print the fruit name and the number of transactions.

   Hint: Consider using a dictionary to keep track of fruit counts.

6. Calculate average transaction value:

   - Compute the average value of all transactions (price \* quantity).
   - Print the result rounded to two decimal places.

   Hint: You'll need to keep a running sum and count of transactions.

7. Identify the biggest spender:

   - Find the person who spent the most money on "bought" transactions.
   - Print their name and the total amount they spent.

   Hint: Another good use case for a dictionary!

8. Write a summary report:

   - Create a new file called `transaction_summary.txt`.
   - Write a summary of your findings (total sales, most popular fruit, average transaction value, biggest spender) to this file.

   Hint: Use the `with` statement again, but this time open the file in write mode.

## Bonus Challenge

If you finish early, try to create a simple bar chart using ASCII characters to visualize the popularity of each fruit.

Remember to add comments to your code explaining what each section does. Good luck!
