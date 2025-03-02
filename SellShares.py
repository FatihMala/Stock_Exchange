import os

STOCK_FILE = "YOUR OWN FILE PATH"  # Update your own file path
STOCK_TRANSACTION = "YOUR OWN FILE PATH"  # Update your own file path

def SellShares():
    stock_map = {}

    # Open file to read shares
    if os.path.exists(STOCK_FILE):
        with open(STOCK_FILE, "r") as file:
            for line in file:
                stock_details = line.strip().split(",")
                stock_map[stock_details[0]] = stock_details

    
    for_sell_name = input("Enter the name of the stock to sell: ")
    if for_sell_name in stock_map:
        existing_details = stock_map[for_sell_name]
        existing_price = float(existing_details[1])
        existing_quantity = int(existing_details[2])
        existing_total_value = float(existing_details[3])

        sell_stock_price = float(input("Enter the selling price of the stock: "))
        sell_stock_quantity = int(input("Enter the quantity to sell: "))
        sell_stock_date = input("Enter the selling date (YYYY-MM-DD): ")

        sell_total_value = sell_stock_price * sell_stock_quantity
        status = 0  

        if sell_stock_quantity <= 0:
            print("The quantity cannot be 0 or less.")
            return
        elif sell_stock_quantity < existing_quantity:
            # Updated stock information
            new_quantity = existing_quantity - sell_stock_quantity
            new_total_value = existing_total_value - (sell_stock_quantity * sell_stock_price)
            new_price = new_total_value / new_quantity
            status = (sell_stock_price - existing_price) * sell_stock_quantity

            if status > 0:
                print(f"You are in profit from {for_sell_name}. Your profit is {status:.2f}")
            else:
                print(f"You are at loss from {for_sell_name}. Your loss is {status:.2f}")

            stock_map[for_sell_name] = [for_sell_name, f"{new_price:.2f}", str(new_quantity), f"{new_total_value:.2f}", sell_stock_date]
            log_transaction(for_sell_name, sell_stock_price, sell_stock_quantity, sell_total_value, sell_stock_date, "Sell", status)

        elif sell_stock_quantity == existing_quantity:
            # If the share is sold completely
            status = sell_total_value - existing_total_value
            stock_map.pop(for_sell_name)

            log_transaction(for_sell_name, sell_stock_price, sell_stock_quantity, sell_total_value, sell_stock_date, "Sell", status)

            if status > 0:
                print(f"You are in profit from {for_sell_name}. Your profit is {status:.2f}")
            else:
                print(f"You are at loss from {for_sell_name}. Your loss is {status:.2f}")

        else:
            print("The quantity cannot be more than the current quantity.")
            return

        # Write updated stock information to file
        with open(STOCK_FILE, "w") as file:
            for stock_details in stock_map.values():
                file.write(",".join(stock_details) + "\n")

    else:
        print("This stock is not available.")
        return

    print("You sold stock successfully.")

def log_transaction(for_sell_name, sell_stock_price, sell_stock_quantity, sell_total_value, sell_stock_date, transaction_type, status):
    # Save to transaction history
    with open(STOCK_TRANSACTION, "a") as file:
        file.write(f"{transaction_type}: {for_sell_name},{sell_stock_price},{sell_stock_quantity},{sell_total_value},{sell_stock_date},{status:.2f}\n")
SellShares()