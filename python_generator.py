import random

# Open file in write mode
with open('input.txt', 'w') as f:
    # Generate 1000 lines
    for _ in range(1000):
        # Generate random numbers according to specifications
        num1 = random.randint(1, 1000)    # First column: 1-1000
        num2 = random.randint(5, 100)     # Second column: 5-100
        num3 = random.randint(1, 10)      # Third column: 1-10
        
        # Write the numbers to file with proper formatting
        # Each number is separated by a space
        f.write(f"{num1} {num2} {num3}\n")

print("File 'input.txt' has been generated successfully!")
