import os

STOCK_FILE = "YOUR OWN FILE PATH" #Update your own file path

 

def show_all_stocks():
    
    total_portfolio_value = 0.0

    if not os.path.exists(STOCK_FILE):
        print("Stock file not found.")
        return

    try:
        with open(STOCK_FILE, "r") as file:
            lines = file.readlines()
            output = ["Current stocks:\n"]

            for line in lines:
                stock_details = line.strip().split(",")
                stock_name = stock_details[0]
                stock_price = float(stock_details[1])
                stock_quantity = int(stock_details[2])
                total_value = float(stock_details[3])
                date = stock_details[4]

                # Adding to total portfolio value
                total_portfolio_value += total_value

                # Adding each stock details
                output.append(
                    f"Stock: {stock_name}  -- Price: {stock_price}  -- Quantity: {stock_quantity}  -- Total Value: {total_value}  -- Date: {date}\n"
                )

            # Print total portfolio value at top
            print(f"Total Portfolio Value: {total_portfolio_value:.2f}")
            # Print all share details
            print("".join(output))

    except Exception as e:
        print("An error occurred:", str(e))


show_all_stocks()
