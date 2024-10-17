# Quiz: Output Exercise

## Instructions
1. Read the code snippet carefully.
2. Try to calculate the output in your mind or on paper.
3. Click on the "Answer" dropdown to check your solution.
4. If you need more clarification, click on the "Explanation" dropdown.

---

1. What is the output of the given code below:
```python
x = 5
y = 2
print(x + y)
```

<details>
<summary>Answer</summary>

7

</details>

<details>
<summary>Explanation</summary>

The code adds the values of `x` (5) and `y` (2), resulting in 7, which is then printed.

</details>

---

2. What is the output of the given code below:
```python
text = "Python"
print(text * 3)
```

<details>
<summary>Answer</summary>

PythonPythonPython

</details>

<details>
<summary>Explanation</summary>

The `*` operator with a string and an integer repeats the string that many times. Here, "Python" is repeated 3 times.

</details>

---

3. What is the output of the given code below:
```python
x = 10
y = 3
print(x // y)
```

<details>
<summary>Answer</summary>

3

</details>

<details>
<summary>Explanation</summary>

The `//` operator performs integer division (floor division). 10 divided by 3 is 3 with a remainder, but floor division rounds down to the nearest integer, which is 3.

</details>

---

4. What is the output of the given code below:
```python
x = 5
x += 3
print(x)
```

<details>
<summary>Answer</summary>

8

</details>

<details>
<summary>Explanation</summary>

The `+=` operator adds the right operand to the left operand and assigns the result to the left operand. So, `x += 3` is equivalent to `x = x + 3`, which results in 8.

</details>

---

5. What is the output of the given code below:
```python
print(bool(0), bool(1), bool(""))
```

<details>
<summary>Answer</summary>

False True False

</details>

<details>
<summary>Explanation</summary>

In Python, `0` and empty strings are considered falsy values, while any non-zero number is truthy. Therefore, `bool(0)` is `False`, `bool(1)` is `True`, and `bool("")` is `False`.

</details>

---

6. What is the output of the given code below:
```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)
```

<details>
<summary>Answer</summary>

[1, 2, 3, 4]

</details>

<details>
<summary>Explanation</summary>

Lists are mutable and assigned by reference. When `y = x` is executed, both `x` and `y` refer to the same list. So, when 4 is appended to `y`, it's also reflected in `x`.

</details>

---

7. What is the output of the given code below:
```python
x = "Hello"
y = "World"
print(x[1] + y[1])
```

<details>
<summary>Answer</summary>

eo

</details>

<details>
<summary>Explanation</summary>

String indexing starts at 0. `x[1]` is 'e' (the second character of "Hello"), and `y[1]` is 'o' (the second character of "World"). The `+` operator concatenates these characters.

</details>

---

8. What is the output of the given code below:
```python
x = 5
y = 2
print(x % y)
```

<details>
<summary>Answer</summary>

1

</details>

<details>
<summary>Explanation</summary>

The `%` operator calculates the remainder of division. 5 divided by 2 is 2 with a remainder of 1, so 5 % 2 equals 1.

</details>

---

9. What is the output of the given code below:
```python
x = [1, 2, 3]
print(len(x) + x[1])
```

<details>
<summary>Answer</summary>

5

</details>

<details>
<summary>Explanation</summary>

`len(x)` returns 3 (the length of the list), and `x[1]` is 2 (the second element of the list). The code adds these values: 3 + 2 = 5.

</details>

---

10. What is the output of the given code below:
```python
x = "Python"
print(x[::-1])
```

<details>
<summary>Answer</summary>

nohtyP

</details>

<details>
<summary>Explanation</summary>

The slice notation `[::-1]` reverses the string. It starts from the end (no start index), goes to the beginning (no stop index), and moves with a step of -1 (backwards).

</details>

---

11. What is the output of the given code below:
```python
x = 10
y = 3
print(x % y * 2)
```

<details>
<summary>Answer</summary>

2

</details>

<details>
<summary>Explanation</summary>

First, `x % y` is calculated: 10 % 3 = 1 (the remainder of 10 divided by 3). Then, this result is multiplied by 2: 1 * 2 = 2.

</details>

---

12. What is the output of the given code below:
```python
x = [1, 2, 3]
y = x.copy()
y.append(4)
print(x)
```

<details>
<summary>Answer</summary>

[1, 2, 3]

</details>

<details>
<summary>Explanation</summary>

Unlike the previous list example, `y = x.copy()` creates a new list with the same elements as `x`. Modifying `y` doesn't affect `x`, so `x` remains unchanged.

</details>

---

13. What is the output of the given code below:
```python
x = "Hello"
print(x.replace("l", "L", 1))
```

<details>
<summary>Answer</summary>

HeLlo

</details>

<details>
<summary>Explanation</summary>

The `replace()` method replaces occurrences of a substring with another substring. The third argument (1) limits it to replacing only the first occurrence of "l" with "L".

</details>

---

14. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(x[1:4:2])
```

<details>
<summary>Answer</summary>

[2, 4]

</details>

<details>
<summary>Explanation</summary>

The slice `[1:4:2]` starts at index 1, goes up to (but not including) index 4, and uses a step of 2. This results in selecting elements at indices 1 and 3.

</details>

---

15. What is the output of the given code below:
```python
x = "Python"
y = "Programming"
print(x[0] + y[-1])
```

<details>
<summary>Answer</summary>

Pg

</details>

<details>
<summary>Explanation</summary>

`x[0]` is 'P' (the first character of "Python"), and `y[-1]` is 'g' (the last character of "Programming"). These are concatenated to form "Pg".

</details>

---

16. What is the output of the given code below:
```python
x = 5
y = 2
print(x ** y)
```

<details>
<summary>Answer</summary>

25

</details>

<details>
<summary>Explanation</summary>

The `**` operator performs exponentiation. This code calculates 5 raised to the power of 2, which is 25.

</details>

---

17. What is the output of the given code below:
```python
x = [1, 2, 3]
y = [4, 5, 6]
print(x + y)
```

<details>
<summary>Answer</summary>

[1, 2, 3, 4, 5, 6]

</details>

<details>
<summary>Explanation</summary>

When used with lists, the `+` operator concatenates them, creating a new list containing all elements from both lists in the order they appear.

</details>

---

18. What is the output of the given code below:
```python
x = "Hello"
print(x.find("l"))
```

<details>
<summary>Answer</summary>

2

</details>

<details>
<summary>Explanation</summary>

The `find()` method returns the index of the first occurrence of the substring. In "Hello", the first 'l' is at index 2 (remember, indexing starts at 0).

</details>

---

19. What is the output of the given code below:
```python
x = [1, 2, 3, 2, 1]
print(x.count(2))
```

<details>
<summary>Answer</summary>

2

</details>

<details>
<summary>Explanation</summary>

The `count()` method returns the number of occurrences of an element in the list. The number 2 appears twice in the list, so the output is 2.

</details>

---

20. What is the output of the given code below:
```python
x = "Python"
print(x.lower().upper())
```

<details>
<summary>Answer</summary>

PYTHON

</details>

<details>
<summary>Explanation</summary>

First, `lower()` converts the string to lowercase ("python"), then `upper()` converts it to uppercase ("PYTHON"). The final result is "PYTHON".

</details>

---

21. What is the output of the given code below:
```python
x = [1, 2, 3]
x.extend([4, 5])
print(len(x))
```

<details>
<summary>Answer</summary>

5

</details>

<details>
<summary>Explanation</summary>

The `extend()` method adds all elements of the given list to the end of the original list. After extending, `x` becomes `[1, 2, 3, 4, 5]`, which has a length of 5.

</details>

---

22. What is the output of the given code below:
```python
x = "Hello, World!"
print(x.split(","))
```

<details>
<summary>Answer</summary>

['Hello', ' World!']

</details>

<details>
<summary>Explanation</summary>

The `split()` method splits a string into a list of substrings based on the specified delimiter. Here, it splits at the comma, resulting in two elements.

</details>

---

23. What is the output of the given code below:
```python
x = 5
y = 2
print(f"{x} divided by {y} is {x/y:.2f}")
```

<details>
<summary>Answer</summary>

5 divided by 2 is 2.50

</details>

<details>
<summary>Explanation</summary>

This uses an f-string for formatting. `{x/y:.2f}` formats the result of 5/2 to two decimal places. The `.2f` specifies two digits after the decimal point.

</details>

---

24. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(sum(x[1::2]))
```

<details>
<summary>Answer</summary>

9

</details>

<details>
<summary>Explanation</summary>

The slice `[1::2]` starts at index 1 and takes every second element, resulting in `[2, 4]`. The `sum()` function then adds these numbers: 2 + 4 = 6.

</details>

---

25. What is the output of the given code below:
```python
x = "Python"
y = "Java"
print(sorted(x + y))
```

<details>
<summary>Answer</summary>

[' ', 'a', 'h', 'J', 'n', 'o', 'P', 't', 'v', 'y']

</details>

<details>
<summary>Explanation</summary>

The `sorted()` function returns a new sorted list of the given iterable. Here, it concatenates "Python" and "Java", then sorts all characters alphabetically (with uppercase letters coming before lowercase).

</details>

---

26. What is the output of the given code below:
```python
x = "Hello"
print(x.center(10, "*"))
```

<details>
<summary>Answer</summary>

**Hello***

</details>

<details>
<summary>Explanation</summary>

The `center()` method centers the string within a string of specified length. Here, it centers "Hello" in a 10-character string, filling the extra space with asterisks.

</details>

---

27. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(x[-2:] + x[:2])
```

<details>
<summary>Answer</summary>

[4, 5, 1, 2]

</details>

<details>
<summary>Explanation</summary>

`x[-2:]` slices the last two elements [4, 5], and `x[:2]` slices the first two elements [1, 2]. These are then concatenated.

</details>

---

28. What is the output of the given code below:
```python
x = 5
y = 2
print(f"{x} to the power of {y} is {x**y}")
```

<details>
<summary>Answer</summary>

5 to the power of 2 is 25

</details>

<details>
<summary>Explanation</summary>

This uses an f-string for formatting. `{x**y}` calculates 5 raised to the power of 2, which is 25.

</details>

---

29. What is the output of the given code below:
```python
x = [1, 2, 3]
y = [4, 5, 6]
print(list(zip(x, y)))
```

<details>
<summary>Answer</summary>

[(1, 4), (2, 5), (3, 6)]

</details>

<details>
<summary>Explanation</summary>

The `zip()` function pairs elements from the two lists. `list()` converts the zip object to a list of tuples.

</details>

---

30. What is the output of the given code below:
```python
x = "Python"
print(x.ljust(10, '-') + x.rjust(10, '-'))
```

<details>
<summary>Answer</summary>

Python----    ----Python

</details>

<details>
<summary>Explanation</summary>

`ljust()` left-justifies the string in a 10-character field, filling with '-'. `rjust()` does the same but right-justifies. These are then concatenated.

</details>

---

31. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(x[::2])
```

<details>
<summary>Answer</summary>

[1, 3, 5]

</details>

<details>
<summary>Explanation</summary>

The slice `[::2]` starts at the beginning, goes to the end, and takes every second element.

</details>

---

32. What is the output of the given code below:
```python
x = "Hello"
y = "World"
print(f"{x:>10}{y:<10}")
```

<details>
<summary>Answer</summary>

     HelloWorld     

</details>

<details>
<summary>Explanation</summary>

In the f-string, `:>10` right-aligns "Hello" in a 10-character field, while `:<10` left-aligns "World" in a 10-character field.

</details>

---

33. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(sum(x[1::2]) - sum(x[::2]))
```

<details>
<summary>Answer</summary>

-3

</details>

<details>
<summary>Explanation</summary>

`x[1::2]` is [2, 4], summing to 6. `x[::2]` is [1, 3, 5], summing to 9. 6 - 9 = -3.

</details>

---

34. What is the output of the given code below:
```python
x = "Python"
print(''.join(sorted(set(x.lower()))))
```

<details>
<summary>Answer</summary>

hnopty

</details>

<details>
<summary>Explanation</summary>

`set(x.lower())` creates a set of unique lowercase letters. `sorted()` orders them alphabetically. `''.join()` combines them into a string.

</details>

---

35. What is the output of the given code below:
```python
x = [1, 2, 3]
y = [i*2 for i in x]
print(y)
```

<details>
<summary>Answer</summary>

[2, 4, 6]

</details>

<details>
<summary>Explanation</summary>

This is a list comprehension. It creates a new list `y` where each element is twice the corresponding element in `x`.

</details>

---

36. What is the output of the given code below:
```python
x = "Hello World"
print(x.swapcase())
```

<details>
<summary>Answer</summary>

hELLO wORLD

</details>

<details>
<summary>Explanation</summary>

The `swapcase()` method swaps the case of each character: uppercase becomes lowercase and vice versa.

</details>

---

37. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(x.pop(2))
print(x)
```

<details>
<summary>Answer</summary>

3
[1, 2, 4, 5]

</details>

<details>
<summary>Explanation</summary>

`pop(2)` removes and returns the element at index 2 (which is 3). Then the modified list is printed.

</details>

---

38. What is the output of the given code below:
```python
x = "Python"
print(x.encode())
```

<details>
<summary>Answer</summary>

b'Python'

</details>

<details>
<summary>Explanation</summary>

The `encode()` method returns a bytes object. The 'b' prefix indicates it's a bytes literal.

</details>

---

39. What is the output of the given code below:
```python
x = [1, 2, 3]
y = [4, 5, 6]
z = list(map(lambda a, b: a+b, x, y))
print(z)
```

<details>
<summary>Answer</summary>

[5, 7, 9]

</details>

<details>
<summary>Explanation</summary>

`map()` applies the lambda function (which adds two numbers) to each pair of elements from `x` and `y`. The result is converted to a list.

</details>

---

40. What is the output of the given code below:
```python
x = "Hello"
y = reversed(x)
print(''.join(y))
```

<details>
<summary>Answer</summary>

olleH

</details>

<details>
<summary>Explanation</summary>

`reversed()` returns an iterator that accesses the string's characters in reverse order. `''.join()` combines these characters into a string.

</details>

---

41. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(x[:-1])
```

<details>
<summary>Answer</summary>

[1, 2, 3, 4]

</details>

<details>
<summary>Explanation</summary>

The slice `[:-1]` returns all elements of the list except the last one.

</details>

---

42. What is the output of the given code below:
```python
x = "Python"
print(x.startswith("Py"))
```

<details>
<summary>Answer</summary>

True

</details>

<details>
<summary>Explanation</summary>

The `startswith()` method returns `True` if the string starts with the specified substring, which it does in this case.

</details>

---

43. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
y = filter(lambda a: a % 2 == 0, x)
print(list(y))
```

<details>
<summary>Answer</summary>

[2, 4]

</details>

<details>
<summary>Explanation</summary>

`filter()` applies the lambda function to each element of `x`, keeping only those for which the function returns `True` (even numbers in this case).

</details>

---

44. What is the output of the given code below:
```python
x = "Hello"
y = "World"
print(min(x, y))
```

<details>
<summary>Answer</summary>

Hello

</details>

<details>
<summary>Explanation</summary>

When `min()` is used with strings, it returns the lexicographically smaller string. "Hello" comes before "World" alphabetically.

</details>

---

45. What is the output of the given code below:
```python
x = [1, 2, 3]
y = x * 2
print(y)
```

<details>
<summary>Answer</summary>

[1, 2, 3, 1, 2, 3]

</details>

<details>
<summary>Explanation</summary>

The `*` operator with a list and an integer repeats the list that many times.

</details>

---

46. What is the output of the given code below:
```python
x = "Python Programming"
print(x.count('P'))
```

<details>
<summary>Answer</summary>

2

</details>

<details>
<summary>Explanation</summary>

The `count()` method returns the number of occurrences of a substring in the string. 'P' appears twice in "Python Programming".

</details>

---

47. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(sum(x[1:-1]))
```

<details>
<summary>Answer</summary>

9

</details>

<details>
<summary>Explanation</summary>

The slice `[1:-1]` selects all elements except the first and last, resulting in [2, 3, 4]. The `sum()` function then adds these numbers: 2 + 3 + 4 = 9.

</details>

---

48. What is the output of the given code below:
```python
x = "Python"
print(''.join(reversed(sorted(x))))
```

<details>
<summary>Answer</summary>

ytohnP

</details>

<details>
<summary>Explanation</summary>

First, `sorted(x)` orders the characters alphabetically. Then `reversed()` reverses this order. Finally, `''.join()` combines the characters into a string.

</details>

---

49. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(x[::2] + x[1::2])
```

<details>
<summary>Answer</summary>

[1, 3, 5, 2, 4]

</details>

<details>
<summary>Explanation</summary>

`x[::2]` selects every second element starting from the first: [1, 3, 5]. `x[1::2]` selects every second element starting from the second: [2, 4]. These are then concatenated.

</details>

---

50. What is the output of the given code below:
```python
x = "Hello World"
print(x.replace(" ", "").isalpha())
```

<details>
<summary>Answer</summary>

True

</details>

<details>
<summary>Explanation</summary>

First, `replace(" ", "")` removes the space. Then `isalpha()` checks if all characters in the string are alphabetic, which they are after removing the space.

</details>

---

51. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(x[::-2])
```

<details>
<summary>Answer</summary>

[5, 3, 1]

</details>

<details>
<summary>Explanation</summary>

The slice `[::-2]` starts from the end, moves towards the beginning, and takes every second element.

</details>

---

52. What is the output of the given code below:
```python
x = "Python"
print(x.rjust(10, '*'))
```

<details>
<summary>Answer</summary>

****Python

</details>

<details>
<summary>Explanation</summary>

The `rjust()` method right-justifies the string in a field of width 10, filling the left side with asterisks.

</details>

---

53. What is the output of the given code below:
```python
x = [1, 2, 3]
y = [4, 5, 6]
print(list(map(pow, x, y)))
```

<details>
<summary>Answer</summary>

[1, 32, 729]

</details>

<details>
<summary>Explanation</summary>

`map(pow, x, y)` applies the `pow()` function to each pair of elements from `x` and `y`. So it calculates 1^4, 2^5, and 3^6.

</details>

---

54. What is the output of the given code below:
```python
x = "Hello World"
print(x[::2])
```

<details>
<summary>Answer</summary>

HloWrd

</details>

<details>
<summary>Explanation</summary>

The slice `[::2]` selects every second character from the string, starting from the first character.

</details>

---

55. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(x.index(3))
```

<details>
<summary>Answer</summary>

2

</details>

<details>
<summary>Explanation</summary>

The `index()` method returns the index of the first occurrence of the specified element in the list. The number 3 is at index 2 in the list.

</details>

---

56. What is the output of the given code below:
```python
x = "Python"
print(''.join([i*2 for i in x]))
```

<details>
<summary>Answer</summary>

PPyytthhoonn

</details>

<details>
<summary>Explanation</summary>

This list comprehension doubles each character in the string. Then `''.join()` combines these doubled characters into a single string.

</details>

---

57. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(x[-3:] + x[:-3])
```

<details>
<summary>Answer</summary>

[3, 4, 5, 1, 2]

</details>

<details>
<summary>Explanation</summary>

`x[-3:]` selects the last three elements [3, 4, 5], and `x[:-3]` selects all but the last three elements [1, 2]. These are then concatenated.

</details>

---

58. What is the output of the given code below:
```python
x = "Python"
print(x.zfill(10))
```

<details>
<summary>Answer</summary>

0000Python

</details>

<details>
<summary>Explanation</summary>

The `zfill()` method pads the string on the left with zeros to fill the specified width.

</details>

---

59. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(sum(filter(lambda a: a % 2 != 0, x)))
```

<details>
<summary>Answer</summary>

9

</details>

<details>
<summary>Explanation</summary>

`filter()` keeps only the odd numbers [1, 3, 5], and then `sum()` adds them up: 1 + 3 + 5 = 9.

</details>

---

60. What is the output of the given code below:
```python
x = "Hello"
y = "World"
print(sorted(x + y))
```

<details>
<summary>Answer</summary>

[' ', 'd', 'e', 'H', 'l', 'l', 'l', 'o', 'o', 'r', 'W']

</details>

<details>
<summary>Explanation</summary>

The strings are concatenated, then `sorted()` returns a list of all characters in alphabetical order. Note that uppercase letters come before lowercase in ASCII ordering.

</details>

---

61. What is the output of the given code below:
```python
x = [1, 2, 3]
print(list(enumerate(x, start=10)))
```

<details>
<summary>Answer</summary>

[(10, 1), (11, 2), (12, 3)]

</details>

<details>
<summary>Explanation</summary>

`enumerate()` creates pairs of indices and values. The `start` parameter sets the initial index to 10.

</details>

---

62. What is the output of the given code below:
```python
x = "Python Programming"
print(x.partition("on"))
```

<details>
<summary>Answer</summary>

('Pyth', 'on', ' Programming')

</details>

<details>
<summary>Explanation</summary>

The `partition()` method splits the string at the first occurrence of the specified substring, returning a tuple of the part before the separator, the separator itself, and the part after the separator.

</details>

---

63. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(x[1:4][::-1])
```

<details>
<summary>Answer</summary>

[4, 3, 2]

</details>

<details>
<summary>Explanation</summary>

First, `x[1:4]` selects [2, 3, 4]. Then `[::-1]` reverses this selection.

</details>

---

64. What is the output of the given code below:
```python
x = "Hello World"
print(x.strip('Held'))
```

<details>
<summary>Answer</summary>

o Wor

</details>

<details>
<summary>Explanation</summary>

The `strip()` method removes the specified characters from the beginning and end of the string. It removes 'H' from the start and 'ld' from the end.

</details>

---

65. What is the output of the given code below:
```python
x = [1, 2, 3]
y = [4, 5, 6]
print([a*b for a, b in zip(x, y)])
```

<details>
<summary>Answer</summary>

[4, 10, 18]

</details>

<details>
<summary>Explanation</summary>

This list comprehension multiplies corresponding elements from `x` and `y`: 1*4, 2*5, 3*6.

</details>

---

66. What is the output of the given code below:
```python
x = "Python"
print(x.ljust(10, '*').rjust(15, '-'))
```

<details>
<summary>Answer</summary>

-----Python****

</details>

<details>
<summary>Explanation</summary>

First, `ljust(10, '*')` pads the right side to width 10 with '*'. Then `rjust(15, '-')` pads the left side of the result to width 15 with '-'.

</details>

---

67. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(x[::2] * 2)
```

<details>
<summary>Answer</summary>

[1, 3, 5, 1, 3, 5]

</details>

<details>
<summary>Explanation</summary>

`x[::2]` selects every second element [1, 3, 5], then `* 2` repeats this list twice.

</details>

---

68. What is the output of the given code below:
```python
x = "Python"
print(''.join(sorted(x, key=str.lower)))
```

<details>
<summary>Answer</summary>

hnoPty

</details>

<details>
<summary>Explanation</summary>

`sorted()` with `key=str.lower` sorts the characters alphabetically, ignoring case. `''.join()` then combines them into a string.

</details>

---

69. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(list(map(lambda a: a**2 if a % 2 == 0 else a, x)))
```

<details>
<summary>Answer</summary>

[1, 4, 3, 16, 5]

</details>

<details>
<summary>Explanation</summary>

This `map()` applies a lambda function that squares even numbers and leaves odd numbers unchanged.

</details>

---

70. What is the output of the given code below:
```python
x = "Hello World"
print(x.translate(str.maketrans("o", "0")))
```

<details>
<summary>Answer</summary>

Hell0 W0rld

</details>

<details>
<summary>Explanation</summary>

`str.maketrans()` creates a translation table that replaces "o" with "0". `translate()` then applies this translation to the string.

</details>

---

71. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print([i if i % 2 == 0 else i*2 for i in x])
```

<details>
<summary>Answer</summary>

[2, 2, 6, 4, 10]

</details>

<details>
<summary>Explanation</summary>

This list comprehension doubles odd numbers and leaves even numbers unchanged.

</details>

---

72. What is the output of the given code below:
```python
x = "Python"
print(x.center(10, '*')[1:-1])
```

<details>
<summary>Answer</summary>

**Python*

</details>

<details>
<summary>Explanation</summary>

`center(10, '*')` creates '**Python**'. Then `[1:-1]` slices off the first and last characters.

</details>

---

73. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(list(reversed(x[1::2])))
```

<details>
<summary>Answer</summary>

[5, 3]

</details>

<details>
<summary>Explanation</summary>

`x[1::2]` selects every second element starting from index 1: [2, 4]. `reversed()` then reverses this list.

</details>

---

74. What is the output of the given code below:
```python
x = "Hello World"
print(x.swapcase().title())
```

<details>
<summary>Answer</summary>

Hello World

</details>

<details>
<summary>Explanation</summary>

`swapcase()` changes "Hello World" to "hELLO wORLD". Then `title()` capitalizes the first letter of each word.

</details>

---

75. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(sum(x[1::2]) / len(x[::2]))
```

<details>
<summary>Answer</summary>

2.0

</details>

<details>
<summary>Explanation</summary>

`sum(x[1::2])` sums every second element starting from index 1: 2 + 4 = 6. `len(x[::2])` counts every second element starting from index 0: [1, 3, 5], which is 3. So, 6 / 3 = 2.0.

</details>

---

76. What is the output of the given code below:
```python
x = "Python Programming"
print(x.replace('P', 'J', 1).replace('P', 'j', 1))
```

<details>
<summary>Answer</summary>

Jython jrogramming

</details>

<details>
<summary>Explanation</summary>

The first `replace()` changes the first 'P' to 'J'. The second `replace()` changes the next 'P' to 'j'.

</details>

---

77. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
print([a if a % 2 == 0 else b for a, b in zip(x, y)])
```

<details>
<summary>Answer</summary>

[6, 2, 8, 4, 10]

</details>

<details>
<summary>Explanation</summary>

This list comprehension selects the element from `x` if it's even, otherwise it selects the corresponding element from `y`.

</details>

---

78. What is the output of the given code below:
```python
x = "Python"
print(''.join(x[i] for i in range(len(x)-1, -1, -2)))
```

<details>
<summary>Answer</summary>

nhy

</details>

<details>
<summary>Explanation</summary>

This generator expression selects characters from the end of the string, moving backwards by 2 each time. `''.join()` combines these characters into a string.

</details>

---

79. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(list(filter(lambda a: a > sum(x)/len(x), x)))
```

<details>
<summary>Answer</summary>

[4, 5]

</details>

<details>
<summary>Explanation</summary>

`sum(x)/len(x)` calculates the average of `x`, which is 3. The `filter()` function then keeps only the numbers greater than 3.

</details>

---

80. What is the output of the given code below:
```python
x = "Hello World"
print(x.encode('ascii').decode('ascii'))
```

<details>
<summary>Answer</summary>

Hello World

</details>

<details>
<summary>Explanation</summary>

`encode('ascii')` converts the string to ASCII bytes, then `decode('ascii')` converts it back to a string. Since all characters are ASCII, the string remains unchanged.

</details>

---

81. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(list(map(lambda a: a**2, filter(lambda a: a % 2 != 0, x))))
```

<details>
<summary>Answer</summary>

[1, 9, 25]

</details>

<details>
<summary>Explanation</summary>

First, `filter()` selects odd numbers [1, 3, 5]. Then `map()` applies the square function to each of these numbers.

</details>

---

82. What is the output of the given code below:
```python
x = "Python"
print(''.join(sorted(set(x.lower()), key=x.lower().index)))
```

<details>
<summary>Answer</summary>

python

</details>

<details>
<summary>Explanation</summary>

This creates a set of unique lowercase letters, then sorts them based on their first appearance in the original (lowercase) string.

</details>

---

83. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(sum(i for i in x if i % 2 == 0) - sum(i for i in x if i % 2 != 0))
```

<details>
<summary>Answer</summary>

-3

</details>

<details>
<summary>Explanation</summary>

This calculates the sum of even numbers (2 + 4 = 6) minus the sum of odd numbers (1 + 3 + 5 = 9), resulting in 6 - 9 = -3.

</details>

---

84. What is the output of the given code below:
```python
x = "Hello World"
print(x.translate(str.maketrans("aeiou", "12345")))
```

<details>
<summary>Answer</summary>

H2ll4 W4rld

</details>

<details>
<summary>Explanation</summary>

`str.maketrans()` creates a translation table that replaces vowels with numbers. `translate()` then applies this translation to the string.

</details>

---

85. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print([i if i < 3 else i*2 for i in x])
```

<details>
<summary>Answer</summary>

[1, 2, 6, 8, 10]

</details>

<details>
<summary>Explanation</summary>

This list comprehension doubles numbers greater than or equal to 3, and leaves other numbers unchanged.

</details>

---

86. What is the output of the given code below:
```python
x = "Python Programming"
print(x.lower().count('p'))
```

<details>
<summary>Answer</summary>

2

</details>

<details>
<summary>Explanation</summary>

First, `lower()` converts the string to lowercase. Then `count('p')` counts the occurrences of 'p', which appear twice in "python programming".

</details>

---

87. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(list(zip(x[::2], x[1::2])))
```

<details>
<summary>Answer</summary>

[(1, 2), (3, 4), (5, None)]

</details>

<details>
<summary>Explanation</summary>

`x[::2]` is [1, 3, 5] and `x[1::2]` is [2, 4]. `zip()` pairs these up, adding None when one list runs out of elements.

</details>

---

88. What is the output of the given code below:
```python
x = "Hello"
y = "World"
print(''.join(a+b for a, b in zip(x, y)))
```

<details>
<summary>Answer</summary>

HWeolrllod

</details>

<details>
<summary>Explanation</summary>

This generator expression pairs up characters from `x` and `y`, concatenates each pair, and then `''.join()` combines all these pairs into a single string.

</details>

---

89. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(max(x) - min(x[1::2]))
```

<details>
<summary>Answer</summary>

3

</details>

<details>
<summary>Explanation</summary>

`max(x)` is 5. `x[1::2]` is [2, 4], so `min(x[1::2])` is 2. The difference is 5 - 2 = 3.

</details>

---

90. What is the output of the given code below:
```python
x = "Python"
print(''.join(chr(ord(c) + 1) for c in x))
```

<details>
<summary>Answer</summary>

Qzuipo

</details>

<details>
<summary>Explanation</summary>

This generator expression converts each character to its ASCII value (`ord()`), adds 1, then converts back to a character (`chr()`). This effectively shifts each letter to the next one in the alphabet.

</details>

---

91. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(list(map(lambda a, b: a*b, x, x[::-1])))
```

<details>
<summary>Answer</summary>

[5, 8, 9, 8, 5]

</details>

<details>
<summary>Explanation</summary>

This `map()` multiplies each element of `x` with the corresponding element of `x` reversed. So it computes [1*5, 2*4, 3*3, 4*2, 5*1].

</details>

---

92. What is the output of the given code below:
```python
x = "Hello World"
print(x.replace(' ', '').isalnum())
```

<details>
<summary>Answer</summary>

True

</details>

<details>
<summary>Explanation</summary>

First, `replace(' ', '')` removes the space. Then `isalnum()` checks if all characters in the string are alphanumeric, which they are after removing the space.

</details>

---

93. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print([sum(x[:i+1]) for i in range(len(x))])
```

<details>
<summary>Answer</summary>

[1, 3, 6, 10, 15]

</details>

<details>
<summary>Explanation</summary>

This list comprehension calculates the cumulative sum of the list. For each index, it sums all elements up to and including that index.

</details>

---

94. What is the output of the given code below:
```python
x = "Python"
print(''.join(sorted(x * 2, key=lambda c: (c.lower(), c.isupper()))))
```

<details>
<summary>Answer</summary>

hhnnoooPPttyy

</details>

<details>
<summary>Explanation</summary>

This sorts the characters of "PythonPython" first by lowercase value, then by whether they're uppercase. This groups lowercase before uppercase for each letter.

</details>

---

95. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(list(filter(lambda a: a == len(x) or x.index(a) == a-1, x)))
```

<details>
<summary>Answer</summary>

[1, 5]

</details>

<details>
<summary>Explanation</summary>

This `filter()` keeps elements that are either equal to the length of the list (5) or whose value minus 1 equals their index. This is true for 1 (index 0) and 5 (length of list).

</details>

---

96. What is the output of the given code below:
```python
x = "Hello World"
print(''.join(c.lower() if i % 2 else c.upper() for i, c in enumerate(x)))
```

<details>
<summary>Answer</summary>

HeLlO WoRlD

</details>

<details>
<summary>Explanation</summary>

This generator expression alternates between uppercase and lowercase for each character based on its index.

</details>

---

97. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(sum(map(lambda a, b: a*b, x, range(len(x)))))
```

<details>
<summary>Answer</summary>

40

</details>

<details>
<summary>Explanation</summary>

This `map()` multiplies each element of `x` with its index (0 to 4), resulting in [1*0, 2*1, 3*2, 4*3, 5*4]. The `sum()` function then adds these values: 0 + 2 + 6 + 12 + 20 = 40.

</details>

---

98. What is the output of the given code below:
```python
x = "Python"
print(''.join(c * (i+1) for i, c in enumerate(x)))
```

<details>
<summary>Answer</summary>

Pyythhhoooonnn

</details>

<details>
<summary>Explanation</summary>

This generator expression repeats each character a number of times equal to its index plus one. So 'P' is repeated once, 'y' twice, 't' three times, and so on.

</details>

---

99. What is the output of the given code below:
```python
x = [1, 2, 3, 4, 5]
print(list(accumulate(x)))
```

<details>
<summary>Answer</summary>

[1, 3, 6, 10, 15]

</details>

<details>
<summary>Explanation</summary>

The `accumulate()` function from the `itertools` module (which is assumed to be imported) calculates the cumulative sum of the list.

</details>

---

100. What is the output of the given code below:
```python
x = "Python Programming"
print(len(set(x.lower())))
```

<details>
<summary>Answer</summary>

13

</details>

<details>
<summary>Explanation</summary>

This code first converts the string to lowercase, then creates a set of unique characters. The length of this set is the number of unique characters in the string (including the space).

</details>
