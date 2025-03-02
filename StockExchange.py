
def main_menu():
    while True:
        print('Welcome to Stock Exchange Simulator')
        print('-------------------------------------')
        print('Enter your choice')
        print('1 -> Investor Profile')
        print('2 -> Buy Shares')
        print('3 -> Sell Shares')
        print('4 -> Show the portfolio')
        print('5 -> Show the transaction history')
        print('6 -> Exit')
        choice = input()
        if choice == '1':
            import InvestorProfile
            InvestorProfile.manage_profile()
        elif choice == '2':
            import BuyShares
            BuyShares.BuyShares()
        elif choice == '3':
            import SellShares
            SellShares.SellShares()
        elif choice == '4':
            import ShowPortfolio
            ShowPortfolio.show_all_stocks()
        elif choice == '5':
            import ShowTransaction
            ShowTransaction.show_transactions()
        elif choice == '6':
            print('Exiting the System...')
            exit()
        else:
            print('Invalid choice, please try again.')
            

main_menu()            
    
    
    



