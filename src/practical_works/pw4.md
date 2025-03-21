# Practical 4: Flow Chart and Pseudo Code

## Objective
In this lab, you will implement following  Exercises. This exercise will help you understand the flow chart and pseudo code principles.

**Submission Date:** 

## Prerequisites
- Basic knowledge of Python syntax

## Lab Steps

### Step 1: Download and install Flowgorithm

Get Flowgorithm from the following link
http://www.flowgorithm.org/download/index.html

### Step 2: Implement Basic Sum
Implement the following flow chart, and create python source code

<img width="326" alt="image" src="https://github.com/user-attachments/assets/ca051e86-e905-435a-909a-931292ba7988" />

### Step 3: Implement Largest Number
Implement the following flow chart, and create python source code

<img width="540" alt="image" src="https://github.com/user-attachments/assets/85bded29-52d8-49a7-964d-ef2d17477d62" />

### Step 4: Study Pseudo Code
Binary search is a searching algorithm that works only for sorted search space. It repeatedly divides the search space into half by using the fact that the search space is sorted and checking if the desired search result will be found in the left or right half.
Example: Given a sorted array Arr[] and a value X, The task is to find the index at which X is present in Arr[].
Below is the pseudocode for Binary search.

    BinarySearch(ARR, X, LOW, HIGH)
           repeat till LOW = HIGH
                  MID = (LOW + HIGH)/2
                  if (X == ARR[mid])
                      return MID
                  else if (x > ARR[MID]) 
                      LOW = MID + 1
                  else                  
                      HIGH = MID – 1

### Step 5: Try past midterm question
Design a simple weather data analysis program for a local meteorology station. The program should calculate the average temperature, convert units, and determine temperature ranges.
Create a flowchart and write pseudocode for this system with the following requirements:
● Ask the user to input the highest and lowest temperatures for a day (in Celsius).
● Calculate and display the average temperature for the day.
● Convert the average temperature to Fahrenheit and display it.
Determine and display the temperature range category based on the following criteria:
● If the range (difference between highest and lowest) is less than 10°C: "Stable"
● If the range is between 10°C and 20°C: "Moderate"
● If the range is greater than 20°C: "Volatile"
● If either input temperature is less than -50°C or greater than 50°C, display an error message for invalid input.

## Exercises for Students

1. Implement more complex algorithms in flowgorithm
2. Create Pseudo Code for these two simple algorithms

## Conclusion

In this lab, you've learned flow charts and on looking at pseudo code

Key takeaways:
- 

