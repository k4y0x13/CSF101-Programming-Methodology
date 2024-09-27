# Insertion Sort

# 1. Concept

Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It's much like sorting a hand of playing cards. You start with one card and then insert each subsequent card into its proper position among the cards you've already sorted.

# 2. How Does Insertion Sort Work

Insertion sort works by virtually splitting the array into a sorted and an unsorted part. Values from the unsorted part are picked and placed in the correct position in the sorted part.

The steps are as follows:
1. Start with the second element (index 1) as the key.
2. Compare the key with the elements before it.
3. If the element before the key is greater, move it one position ahead.
4. Repeat step 3 until a smaller (or equal) element is found or the start of the array is reached.
5. Place the key in the correct position.
6. Repeat steps 1-5 for all elements in the array.

# 3. Time / Space Complexity

Time Complexity:
- Worst-case: O(n²) - when the array is in reverse order
- Average-case: O(n²)
- Best-case: O(n) - when the array is already sorted

Space Complexity:
- O(1) - Insertion sort is an in-place sorting algorithm, so it uses only a constant amount of extra space.

# 4. When to Use & When Not to Use Insertion Sort

When to use:
- For small datasets or nearly sorted lists
- When dealing with continuous inflow of numbers and they need to be kept sorted
- When memory usage is a concern (due to its in-place nature)
- For simplicity in implementation

When not to use:
- For large datasets (inefficient for big lists)
- In performance-critical applications with large amounts of data
- When faster algorithms like QuickSort or MergeSort are more suitable
- In scenarios where the data is completely unsorted and large

# 5. Implementing Insertion Sort in Python

Here's a Python implementation of the insertion sort algorithm:

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, 
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr
```

# 6. Example Problem 

Problem: A librarian needs to sort a list of books by their publication year to arrange them chronologically on a shelf.

Example:

```python
def insertion_sort(books):
    for i in range(1, len(books)):
        key = books[i]
        j = i - 1
        while j >= 0 and key['year'] < books[j]['year']:
            books[j + 1] = books[j]
            j -= 1
        books[j + 1] = key
    return books

# List of books with their titles and publication years
books = [
    {"title": "To Kill a Mockingbird", "year": 1960},
    {"title": "Pride and Prejudice", "year": 1813},
    {"title": "1984", "year": 1949},
    {"title": "The Great Gatsby", "year": 1925},
    {"title": "The Catcher in the Rye", "year": 1951}
]

print("Original order:")
for book in books:
    print(f"{book['title']} ({book['year']})")

sorted_books = insertion_sort(books)

print("\nSorted by year:")
for book in sorted_books:
    print(f"{book['title']} ({book['year']})")
```

Output:
```
Original order:
To Kill a Mockingbird (1960)
Pride and Prejudice (1813)
1984 (1949)
The Great Gatsby (1925)
The Catcher in the Rye (1951)

Sorted by year:
Pride and Prejudice (1813)
The Great Gatsby (1925)
1984 (1949)
The Catcher in the Rye (1951)
To Kill a Mockingbird (1960)
```

This example demonstrates how insertion sort can be used to sort a list of books by their publication year, allowing the librarian to arrange them chronologically.
