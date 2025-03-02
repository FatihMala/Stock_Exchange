import os

STOCK_FILE = "YOUR OWN FILE PATH"  # Update your own file path
STOCK_TRANSACTION = "YOUR OWN FILE PATH"  # Update your own file path

def BuyShares():
    StockName = input("Enter Stock Name: ")
    StockPrice = float(input("Enter Stock Price: "))
    StockQuantity = int(input("Enter Stock Quantity: "))
    Date = input("Enter Date (YYYY-MM-DD): ")
    
    StockTotal = StockQuantity * StockPrice
    StockMap = {}
    
    # Read the file and add existing data to the map
    if os.path.exists(STOCK_FILE):
        with open(STOCK_FILE, 'r', encoding="utf-8") as file:
            for line in file:
                stockDetails = line.strip().split(",")
                StockMap[stockDetails[0]] = stockDetails
    
    # Existing shares are updated or new shares are added
    if StockName in StockMap:
        existingDetails = StockMap[StockName]
        existingPrice = float(existingDetails[1])
        existingQuantity = int(existingDetails[2])
        existingTotal = float(existingDetails[3])
        
        new_Quantity = existingQuantity + StockQuantity
        new_Total = existingTotal + StockTotal
        Average_Price = (existingTotal + StockTotal) / new_Quantity  # Average price calculation
        
        StockMap[StockName] = [StockName, f"{Average_Price:.2f}", str(new_Quantity), f"{new_Total:.2f}", Date]
    else:
        StockMap[StockName] = [StockName, f"{StockPrice:.2f}", str(StockQuantity), f"{StockTotal:.2f}", Date]
    
    # Record the share purchase transaction
    log_transaction(StockName, StockPrice, StockQuantity, StockTotal, Date)
    
    # Writing all shares to file
    with open(STOCK_FILE, "w", encoding="utf-8") as file:
        for stockDetails in StockMap.values():
            file.write(",".join(stockDetails) + "\n")
    
    print("You bought stock successfully.")

def log_transaction(StockName, StockPrice, StockQuantity, StockTotal, Date):
    # Adding the transaction to the transaction file
    with open(STOCK_TRANSACTION, 'a', encoding="utf-8") as file:
        file.write(f"Buy: {StockName},{StockPrice:.2f},{StockQuantity},{StockTotal:.2f},{Date}\n")
