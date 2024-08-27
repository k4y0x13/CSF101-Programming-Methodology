# Solution for Fruit Transaction Analysis Challenge

def read_and_process_data(filename):
    processed_data = []
    with open(filename, 'r') as file:
        for line in file:
            name, action, quantity, item, price = line.strip().split(',')
            processed_data.append({
                'name': name,
                'action': action,
                'quantity': int(quantity),
                'item': item,
                'price': float(price)
            })
    return processed_data

def calculate_total_sales(data):
    return sum(transaction['quantity'] * transaction['price'] 
               for transaction in data if transaction['action'] == 'sold')

def find_most_popular_fruit(data):
    fruit_counts = {}
    for transaction in data:
        fruit_counts[transaction['item']] = fruit_counts.get(transaction['item'], 0) + 1
    most_popular = max(fruit_counts, key=fruit_counts.get)
    return most_popular, fruit_counts[most_popular]

def calculate_average_transaction_value(data):
    total_value = sum(transaction['quantity'] * transaction['price'] for transaction in data)
    return round(total_value / len(data), 2)

def identify_biggest_spender(data):
    spending = {}
    for transaction in data:
        if transaction['action'] == 'bought':
            name = transaction['name']
            amount = transaction['quantity'] * transaction['price']
            spending[name] = spending.get(name, 0) + amount
    biggest_spender = max(spending, key=spending.get)
    return biggest_spender, round(spending[biggest_spender], 2)

def create_ascii_bar_chart(data):
    fruit_counts = {}
    for transaction in data:
        fruit_counts[transaction['item']] = fruit_counts.get(transaction['item'], 0) + 1
    
    max_count = max(fruit_counts.values())
    chart = ""
    for fruit, count in sorted(fruit_counts.items()):
        bar_length = int((count / max_count) * 20)
        chart += f"{fruit.ljust(10)} | {'#' * bar_length} ({count})\n"
    return chart

def main():
    data = read_and_process_data('fruit_transactions.txt')
    
    total_sales = calculate_total_sales(data)
    most_popular_fruit, popularity_count = find_most_popular_fruit(data)
    avg_transaction_value = calculate_average_transaction_value(data)
    biggest_spender, amount_spent = identify_biggest_spender(data)
    
    print(f"Total sales: ${total_sales:.2f}")
    print(f"Most popular fruit: {most_popular_fruit} ({popularity_count} transactions)")
    print(f"Average transaction value: ${avg_transaction_value}")
    print(f"Biggest spender: {biggest_spender} (${amount_spent})")
    
    with open('transaction_summary.txt', 'w') as summary_file:
        summary_file.write(f"Fruit Transaction Analysis Summary\n")
        summary_file.write(f"===================================\n")
        summary_file.write(f"Total sales: ${total_sales:.2f}\n")
        summary_file.write(f"Most popular fruit: {most_popular_fruit} ({popularity_count} transactions)\n")
        summary_file.write(f"Average transaction value: ${avg_transaction_value}\n")
        summary_file.write(f"Biggest spender: {biggest_spender} (${amount_spent})\n")
        summary_file.write(f"\nFruit Popularity Chart:\n")
        summary_file.write(create_ascii_bar_chart(data))

if __name__ == "__main__":
    main()