import os

def show_transactions():
    TRANSACTION_FILE = "YOUR OWN FILE PATH"  # Update your own file path
    
    buy_transactions = []
    sell_transactions = []
    
    if not os.path.exists(TRANSACTION_FILE):
        print("Transaction file not found!")
        return
    
    try:
        with open(TRANSACTION_FILE, "r", encoding="utf-8") as file:
            for line in file:
                details = line.strip().split(",")
                transaction_type, stock_name = details[0].split(":")
                stock_name = stock_name.strip()
                
                if transaction_type == "Buy":
                    buy_transactions.append(details)
                elif transaction_type == "Sell":
                    sell_transactions.append(details)
                else:
                    print(f"Unknown transaction type: {details[0]}")
    
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    print("Buy Transactions:")
    for transaction in buy_transactions:
        print_transaction_details(transaction)
    
    print("\nSell Transactions:")
    for transaction in sell_transactions:
        print_transaction_details(transaction)

def print_transaction_details(details):
    transaction_type, stock_name = details[0].split(":")
    stock_name = stock_name.strip()
    price = details[1]
    quantity = details[2]
    total_value = details[3]
    date = details[4]
    
    output = (
        f"Stock: {stock_name}  -- Price: {price}  -- Quantity: {quantity}  "
        f"-- Total Value: {total_value}  -- Date: {date}"
    )
    
    if transaction_type == "Sell":
        profit_or_loss = details[5] if len(details) > 5 else "N/A"
        output += f"\nProfit/Loss: {profit_or_loss}"
    
    print(output)
    print()

if __name__ == "__main__":
    show_transactions()

