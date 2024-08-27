import random

def generate_input_file(filename, num_lines):
    actions = ["bought", "sold", "traded", "lost", "found"]
    items = ["apples", "bananas", "oranges", "grapes", "pears"]
    
    with open(filename, 'w') as f:
        for _ in range(num_lines):
            name = f"Person{random.randint(1, 100)}"
            action = random.choice(actions)
            item = random.choice(items)
            quantity = random.randint(1, 10)
            price = round(random.uniform(0.5, 5.0), 2)
            
            line = f"{name},{action},{quantity},{item},{price}\n"
            f.write(line)

# Generate the input file
generate_input_file('fruit_transactions.txt', 1000)
print("Input file 'fruit_transactions.txt' has been generated.")